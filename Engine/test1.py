import peng
import time 
import numpy as np
e = peng
bl =[300,0,
    0,400,
    500,500]
b = e.c_polygon(bl,fil="red",out = "black")
al =[0,0,
    300,300,
    200,100]
a = e.c_polygon(al,fil="green",out = "black")
c = e.ck_polygon(a,b)
if type(c) == np.array:
    print("no")
else: 
    print(c)
    c = list(c)
    b = e.c_polygon(c,fil="yellow",out = "blue")
e.reload()
input("end?")