import turtle
t = turtle.Turtle()
positions=[[0,0,"green"],[-240,0,"yellow"],[120,120,"red"],[-120,120,"black"],[-360,120,"blue"]]
t.pensize(5)   #각원의 중심좌표와 색상
for x,y,color in positions:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color,color)
    t.circle(120)
