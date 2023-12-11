from turtle import *
import random
import time

# Khai báo hàm vẽ Mũ Ông già Noel
def drawHat():
    pen.speed(1)
    pen.color('red')
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(3):
        pen.fd(50)
        pen.right(120)
    pen.end_fill()
    for i in range(6):
        pen.dot(10,'white')
        pen.fd(10)
    pen.right(130)
    pen.fd(55)
    pen.dot(10,'white')

# Chiều rộng và chiều cao của đối tượng Cây
n = 170
speed("fastest")
left(90)
forward(3*n)

# Thiết lập màn hình thẻ chúc mừng
card = Screen()
card.setup(1.0, 1.0, 0, 0)
card.title("Nguyễn Trường Uy!")
colors = ['#92b6f0', '#d95d78', '#5cdbb5', '#5ccde0', '#e0d758', '#ed9277']
card.bgcolor(random.choice(colors))
time.sleep(2)

# Màu của cây thông
color("dark green")

# Vẽ ngược các tọa độ thiết kế
backward(n*4.8)
tracer(8, 50)  # Bật/tắt animation và thiết lập độ trễ

# Hàm vẽ Cây Giáng Sinh
def tree(d, s):
    if d <= 0:
        return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)

# Hàm tạo tuyết rơi
def makeSnow():
    for i in range(50):
        snow = Turtle()
        snow.pu()
        snow.color("white")
        snow.shape("circle")
        snow.speed(0)
        snow.goto(random.randint(-700, 700), random.randint(-700, 700))
        snow.dot(7, 'white')
        snowlist.append(snow)

# Hiệu ứng tuyết rơi
def snowfall():
    for i in snowlist:
        i.goto(random.randint(-700, 700), random.randint(-700, 700))
        i.dot(7, 'white')

# Gọi hàm tạo tuyết
snowlist = []
makeSnow()
time.sleep(1)

# Vẽ tiêu đề "Merry Christmas"
pen = Turtle()
pen.speed(10)
pen.left(270)
pen.penup()
pen.forward(400)
pen.color("black")
pen.setx(-395)
pen.color('Yellow')
pen.write("Merry Christmas!!", font=("ravie", 40, "italic"), align="left")

# Gọi hàm vẽ Mũ Ông già Noel
pen.setheading(0)
pen.speed(1)
pen.fd(850)
pen.left(145)
pen.fd(40)
time.sleep(1)
drawHat()

# Vẽ cây thông
tree(15, n)

card.tracer(False)
card.tracer(True)

# Vòng lặp hiệu ứng tuyết rơi và đổi màu nền
while True:
    snowfall()
    card.bgcolor(random.choice(colors))

backward(n/2)
bye()
