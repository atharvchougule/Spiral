#NiceHexSpiral.py
import turtle   
import random
import time
colors = ['red', 'purple', 'blue',
        'green', 'yellow', 'orange', 'violet', 'white', 'gold']
n_o_s = int(turtle.numinput("Number of sides",
                                        "How many sides in your spiral?", 5))
t=turtle.Turtle()
t.shape('turtle')
t.speed(0)
turtle.bgcolor('black')
for x in range(1440+n_o_s):
        t.pencolor(colors[x%9])
        t.width(x/100+5)
        t.forward(x)        
        t.left(360/n_o_s)
        t.right(720/n_o_s)
        t.pencolor(colors[x%9])
        t.width(x/340+1)
        t.backward(x)
        t.left(144)
