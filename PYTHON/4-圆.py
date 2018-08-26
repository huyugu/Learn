def square(t, length, n, m):
    import turtle
    t = turtle.Turtle()
    for i in range(m):
        t.fd(length)
        t.lt(360.0 / n)
    turtle.mainloop()


square("bob", 2, 360, 250)
