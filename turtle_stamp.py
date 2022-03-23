import turtle
import random

def ScreenLeftClick(x,y): #왼쪽 마우스버튼을 클릭해 랜덤 도장찍는 함수
    global r,g,b
    tSize = random.randrange(1, 10) #크기는 1~10
    turtle.shapesize(tSize)
    tAngle = random.randrange(0,360)  # 각도는 0~360도
    turtle.left(tAngle)
    turtle.color((r,g,b))  # 색상
    turtle.penup()
    turtle.goto(x,y)  #이동하고 도장찍기
    turtle.stamp()

    r = random.random()
    g = random.random()
    b = random.random()

pSize = 10
r, g, b = 0.0, 0.0, 0.0    # 변수 초기값

turtle.shape('turtle')

turtle.onscreenclick(ScreenLeftClick, 1)

turtle.done()