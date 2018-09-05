def square(t, length, n):
    import turtle
    import math
    f = math.cos(math.radians(90 - 180 / n))
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(90 + 180 / n)
        t.fd(length / 2 / f)
        t.pu
        t.lt(180)
        t.fd(length / 2 / f)
        t.lt(90 + 180 / n)

    turtle.mainloop()


square("bob", 100, 6)
