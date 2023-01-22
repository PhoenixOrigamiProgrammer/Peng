import peng
import time 
import numpy as np
e = peng
bl =[300,0,
    0,400,
    500,500]
b = e.create_polygon(bl,fil="red",out = "black")
al =[0,0,
    300,300,
    200,100]
a = e.create_polygon(al,fil="green",out = "black")
c = e.colision_polygon(a,b)
if type(c) == np.array:
    print(c)
    c = list(c)
    b = e.create_polygon(c,fil="yellow",out = "blue")
else: 
    print("no")
e.reload()
input("end?")