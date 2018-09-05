import turtle
import math


def koch(t, x, n):
    if n < 3:
        t.fd(x * n)
        return
    m = n / 3.0
    koch(t, x, m)
    t.lt(60)
    koch(t, x, m)
    t.rt(120)
    koch(t, x, m)
    t.lt(60)
    koch(t, x, m)


def s_3(t, x, n):
    t.pu()
    t.lt(150)
    t.fd(x * 3**n / 2 / math.cos(math.radians(30)))
    t.rt(150)
    t.pd()
    for i in range(3):
        koch(t, x, 3**n)
        t.rt(120)


bob = turtle.Turtle()
bob.pencolor("red")
bob.speed(10)

s_3(bob, 10, 2)
turtle.mainloop()
