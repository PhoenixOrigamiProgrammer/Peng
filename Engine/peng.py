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
    def create_line(self,x1,y1,x2,y2,w): #create linien
        l = self.cv.create_line(x1,y1,x2,y2,width=w)
        return(np.array([x1,y1,x2,y2,l]))
    def move_line(self, line, x,y):   #move linien
        cvline = line[4]
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        x3 = (x1+x2)/2
        y3 = (x1+x2)/2
        self.cv.move(cvline,x3+x,y3+y)
        return np.array([cvline, x1+x, y1+y, x2+x, y2+y])
    def colision_line(self,line1,line2):   #colision detektion lines
        x1 = line1[0]- line1[2]  #turn it into fx1*x+f1=fx2*x+f2 format
        y1 = line1[1]- line1[3]
        functionx1 = y1/x1
        x01 = line1[1] * functionx1
        functiony1 = x01-line1[0]
        x2 = line2[0]- line2[2]
        y2 = line2[1]- line2[3]
        functionx2 = y2/x2
        x02 = line2[1] * functionx2
        functiony2 = x02-line2[0]
        solutionx = (functiony1-functiony2)/(functionx1-functionx2)     #solve it
        solutiony = solutionx*functionx1
        if ((line1[0]<solutionx<line1[2] or line1[0]>solutionx>line1[2]) and (line2[0]<solutionx<line2[2] or line2[0]>solutionx>line2[2])) and ((line1[1]<solutionx<line1[3] or line1[1]>solutionx>line1[3]) and (line2[1]<solutiony<line2[3] or line2[1]>solutiony>line2[3])):
            return(np.array([solutionx,solutiony])) 
        else:
            return("no")
    def create_polygon(self,list,fill,out):  #polygon creating
        a = self.cv.create_polygon(list,fill=fill, outline=out)
        return([a,list])
    def colision_polygon(self,polygon1,polygon2): #colision detektion polygon
        polygonlist1 = polygon1[1]
        polygonlist2 = polygon2[1]
        solution = list()
        pline1 = list()
        pline2 = list()
        for counter in range(int(len(polygonlist1)/2)):    #make list of lines
            linelist = list()
            counter +=1
            counter*=2
            linelist.append(polygonlist1[counter-1])
            linelist.append(polygonlist1[counter-2])
            if counter == 0:
                linelist.append(polygonlist1[len(polygonlist1)-1])
                linelist.append(polygonlist1[len(polygonlist1)-2])
            else:
                linelist.append(polygonlist1[counter-3])
                linelist.append(polygonlist1[counter-4])
            pline1.append(linelist)
            create_line(linelist[0],linelist[1],linelist[2],linelist[3],10)
        for counter in range(int(len(polygonlist2)/2)):
            linelist = list()
            counter+=1
            counter*=2
            linelist.append(polygonlist2[counter-1])
            linelist.append(polygonlist2[counter-2])
            if counter == 0:
                linelist.append(polygonlist2[len(polygonlist2)-1])
                linelist.append(polygonlist2[len(polygonlist2)-2])
            else:
                linelist.append(polygonlist2[counter-3])
                linelist.append(polygonlist2[counter-4])
            pline2.append(linelist)
            create_line(linelist[0],linelist[1],linelist[2],linelist[3],10)
        for counteri in range(len(pline1)):   #crosspoints
            for counterj in range(len(pline2)):
                a = self.colision_line(pline1[counteri],pline2[counterj])
                if type(a) == np.array:
                    solution.extend(a)
                else:
                    pass
        '''for counterq in pline1:    #find corners of a polygon in the other
            functiony = counterq[1]    #making a ray
            chekx = counterq[0]
            l = list()
            for r in range(len(pline2)):
                line = pline2[r]  #find crosspoints
                x1 = line[0]- line[2]
                y1 = line[1]- line[3]
                functionx = y1/x1
                x01 = line[1] * functionx
                functiony1 = x01-line[0]
                if functionx != 0:
                    sx = (functiony1-functiony)/(functionx)     #solve it
                    if (line[0]<sx<line[2] or line[0]>sx>line[2]) and (line[1]<functiony<line[3] or line[1]>functiony>line[3]):
                        l.append([sx,functiony])
            counterk = 0
            for countere in l:
                if countere[0]>counterq[0]:
                    counterk += 1
            counterk -= 1
            if counterk // 2:
                solution.extend(counterq)'''
        if len(solution)==0:
            return("no")
        else:
            return(np.array(solution))
    def reload(self):   #cv.updeate
        self.cv.update()
    def c_point(self,x,y):  #punkt createn
        a = self.cv.create_oval(x+2,y+2,x-2,x-2, fill = "red")
        return(np.array([x,y,a]))
root = tk.Tk()
root.title("CTD")
app = engine(root)
app.mainloop
def create_line(x1,y1,x2,y2,w=5):    #make it less frustrating
    a = app.create_line(x1,y1,x2,y2,w)
    return(a)
def reload():
    app.reload()
def create_point(x,y):
    a = app.c_point(x,y)
    return(a)
def colision_line(l1,l2):
    a = app.colision_line(l1,l2)
    return(a)
def create_polygon(list,fil,out):
    a = app.create_polygon(list,fil,out)
    return(a)
def colision_polygon(p1,p2):
    a = app.colision_polygon(p1,p2)
    return(a)
def move_line(l, x,y):
    a = app.move_line(l, x,y)
    return(a)