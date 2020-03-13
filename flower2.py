import turtle
def draw_triangle(triangle):
    i=0
    while(i<3):
        triangle.left(120)
        triangle.forward(100)
       
        i+=1
def draw_square():
    window=turtle.Screen()
    #window.bgcolor("red")

    '''brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(3)
    i=0
    while(i<4):
        brad.forward(100)
        brad.right(90)
        i+=1
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    #第二個參數 角度,第三個參數要轉幾次
    angie.circle(100,360,3)'''

    triangle=turtle.Turtle()
    print(turtle.screensize())
    triangle.shape("turtle")
    #triangle.color("red")
    triangle.penup()
    triangle.goto(180,90)
    triangle.pendown()
    triangle.color("green")
    triangle.speed(1)
    j=0
    while(j<36):
        draw_triangle(triangle)
        triangle.right(190)
        triangle.forward(100)
        j+=1
    triangle.backward(50)
    triangle.right(90)
    triangle.forward(200)
    

    triangle.penup()
    triangle.goto(-100,0)
    triangle.pendown()
    triangle.color("green")
    j=0
    while(j<36):
        draw_triangle(triangle)
        triangle.right(10)
        j+=1
    triangle.goto(-100,0)
    #triangle.right(90)
    triangle.forward(200)
    
    window.exitonclick()
    
draw_square()


