import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.penup()
t.goto(-100, -100)
t.pendown()
for i in range(4):
    t.fd(200)
    t.lt(90)

t.penup()
t.goto(110, 90)
t.lt(135)
t.pendown()
t.fd(156)
t.lt(90)
t.fd(156)
t.penup()
t.home()
t.lt(90)
t.pendown()
for h in range(4):
    t.fd(60)
    t.lt(90)

t.fd(30)
t.lt(90)
t.fd(60)
t.rt(180)
t.fd(30)
t.rt(90)
t.fd(30)
t.rt(180)
t.fd(60)
