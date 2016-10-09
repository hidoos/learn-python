import turtle
import math 

def square(t, length = 10):
    index = 0
    while index < 4:
        t.fd(length)
        t.lt(90)
        index = index + 1
    ### t is turtle , a function draw square

def polygon(t, n = 4, length = 50):
    index = 0
    radain = 360.0 / n
    while index < n:
        t.fd(length)
        t.lt(radain)
        index = index + 1

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


bob = turtle.Turtle()
circle(bob, 100)
turtle.mainloop()
