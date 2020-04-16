import turtle
def drawtriangle():
    for i in range(0,3):
      turtle.right(120)
      turtle.forward(100)

for i in range(1,19):
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    drawtriangle()
    turtle.left(20)
    

