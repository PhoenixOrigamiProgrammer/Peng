import peng
import time 
e = peng
a = e.c_polygon([0,0,300,300,200,100],fill="green",out = "black")
b = e.c_polygon([300,0,0,300,500,500],fill="red",out = "black")
c = e.ck_polygon(a,b)
if c == "no":
    print("no")
else: 
    print(c)
    b = e.c_polygon(c,fill="yellow",out = "blue")
e.reload()
input("end?")