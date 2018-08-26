import turtle


def square(t,length,n):
    import turtle
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
    turtle.mainloop()


square("bob",120,6)
