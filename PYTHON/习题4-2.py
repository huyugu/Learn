def square(t, length, m,n):
    import turtle
    t = turtle.Turtle()
    for x in range(m):
        t.rt(180+360/m*(n-1))           
        for i in range(20*n):
            t.fd(length)
            t.lt(18/m)

        t.lt(180-360/m*n)
        for i in range(20*n):
                t.fd(length)
                t.lt(18/m) 
    turtle.mainloop()


square("bob", 4, 6,3)
