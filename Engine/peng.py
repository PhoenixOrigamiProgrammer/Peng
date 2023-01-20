import numpy as np #all imports
import pandas as pd
import math as m
import tkinter as tk
import time
import vulcan as v

class engine(tk.Frame):
    def __init__(self,master):
        super().__init__(master)    #prepare
        self.pack
        self.x = 1300
        self.y = 650
        self.xm = self.x / 2
        self.ym = self.y / 2
        self.cv = tk.Canvas(width=self.x, height=self.y, bg="white")
        self.cv.pack()
        self.quit = False
    def c_line(self,x1,y1,x2,y2,w): #create linien
        l = self.cv.create_line(x1,y1,x2,y2,width=w)
        return(np.array([x1,y1,x2,y2,l]))
    def move_l(self, l, x,y):   #move linien
        line = l[4]
        x1 = l[0]
        y1 = l[1]
        x2 = l[2]
        y2 = l[3]
        x3 = (x1+x2)/2
        y3 = (x1+x2)/2
        self.cv.move(line,x3+x,y3+y)
        return np.array([line, x1+x, y1+y, x2+x, y2+y])
    def ck_l(self,l1,l2):   #colision detektion lines
        ux1 = l1[0]- l1[2]  #turn it into fx1*x+f1=fx2*x+f2 format
        uy1 = l1[1]- l1[3]
        fx1 = uy1/ux1
        x01 = l1[1] * fx1
        f1 = x01-l1[0]
        ux2 = l2[0]- l2[2]
        uy2 = l2[1]- l2[3]
        fx2 = uy2/ux2
        x02 = l2[1] * fx2
        f2 = x02-l2[0]
        sx = (f1-f2)/(fx1-fx2)     #solve it
        sy = sx*fx1
        if (l1[0]<sx<l1[2] or l1[0]>sx>l1[2]) and (l2[0]<sx<l2[2] or l2[0]>sx>l2[2]):
            return(np.array([sx,sy])) 
        else:
            return("no")
    def c_polygon(self,list,fill,out):  #polygon creating
        print(list)
        a = self.cv.create_polygon(list,fill=fill, outline=out)
        return([a,list])
    def ck_polygon(self,l1,l2): #colision detektion polygon
        t1 = l1[1]
        t2 = l2[1]
        s = list()
        tl1 = list()
        tl2 = list()
        for g in range(int(len(t1)/2)):    #make list of lines
            a = list()
            g*=2
            a.append(t1[g])
            a.append(t1[g-1])
            if g == 0:
                a.append(t1[len(t1)-1])
                a.append(t1[len(t1)-2])
            else:
                a.append(t1[g-2])
                a.append(t1[g-3])
            tl1.append(a)
        for g in range(int(len(t2)/2)):
            a = list()
            g*=2
            a.append(t2[g])
            a.append(t2[g-1])
            if g == 0:
                a.append(t2[len(t2)-1])
                a.append(t2[len(t2)-2])
            else:
                a.append(t2[g-2])
                a.append(t2[g-3])
            tl2.append(a)
        for i in range(len(tl1)):   #crosspoints
            for j in range(len(tl2)):
                a = self.ck_l(tl1[i],tl2[j])
                if type(a) == np.array:
                    s.extend(a)
                else:
                    pass
        for q in tl1:    #find corners of a polygon in the other
            f = q[1]    #making a ray
            x = q[0]
            l = list()
            for r in range(len(tl2)):
                self.line = tl2[r]  #find crosspoints
                p1 = [self.line[0],self.line[1],self.line[2],self.line[3]]
                ux1 = p1[0]- p1[2]
                uy1 = p1[1]- p1[3]
                fx1 = uy1/ux1
                x01 = p1[1] * fx1
                f1 = x01-p1[0]
                if fx1 != 0:
                    sx = (f1-f)/(fx1)     #solve it
                    if p1[0]<sx<p1[2] or p1[0]>sx>p1[2]:
                        l.append([sx,f])
            k = 0
            for e in l:
                if e[0]>q[0]:
                    k += 1
            k -= 1
            if k // 2:
                s.extend(q)
        return(np.array(s))
    def reload(self):   #cv.updeate
        self.cv.update()
    def c_point(self,x,y):  #punkt createn
        a = self.cv.create_oval(x+2,y+2,x-2,x-2, fill = "red")
        return(np.array([x,y,a]))
root = tk.Tk()
root.title("Game")
app = engine(root)
app.mainloop
def c_line(x1,y1,x2,y2,w=5):    #make it less frustrating
    a = app.c_line(x1,y1,x2,y2,w)
    return(a)
def reload():
    app.reload()
def c_point(x,y):
    a = app.c_point(x,y)
    return(a)
def ck_l(l1,l2):
    a = app.ck_l(l1,l2)
    return(a)
def c_polygon(list,fil,out):
    a = app.c_polygon(list,fil,out)
    return(a)
def ck_polygon(p1,p2):
    a = app.ck_polygon(p1,p2)
    return(a)
def move_l(l, x,y):
    a = app.reload(l, x,y)
    return(a)
