import turtle
def draw_triangle(triangle):
    i=0
    triangle.begin_fill()
    while(i<3):
        triangle.left(120)
        triangle.forward(300)
        i+=1
    triangle.fillcolor("#FF4D40")
    triangle.end_fill()
def draw_triangleS(triangle):
    i=0
    triangle.begin_fill()
    while(i<3):
        triangle.right(120)
        triangle.forward(150)      
        i+=1
    triangle.fillcolor("#FFFFFF")
    triangle.end_fill()
def draw_triangleSS(triangle):
    i=0
    triangle.begin_fill()
    while(i<3):
        triangle.right(120)
        triangle.forward(75)      
        i+=1
    triangle.fillcolor("#FFFFFF")
    triangle.end_fill()

def draw_triangleSSS(triangle):
    i=0
    triangle.begin_fill()
    while(i<3):
        triangle.right(120)
        triangle.forward(37.5)      
        i+=1
    triangle.fillcolor("#FFFFFF")
    triangle.end_fill()

    
def draw_square():
    #window=turtle.Screen()
   
    triangle=turtle.Turtle()
    triangle.shape("turtle")
    triangle.penup()
    triangle.pendown()
    triangle.color("green")
    triangle.speed("slowest")
    
    draw_triangle(triangle)

    
    triangle.penup()
    triangle.backward(150)
    triangle.left(120)
    triangle.forward(150)    
    triangle.pendown()
    draw_triangleS(triangle)

    triangle.penup()
    triangle.backward(75)
    triangle.left(120)
    triangle.forward(75)  
    triangle.pendown()
    draw_triangleSS(triangle)

    
    triangle.penup()
    triangle.right(240)
    triangle.forward(150)
    triangle.left(120)
    triangle.forward(75)  
    triangle.pendown()
    draw_triangleSS(triangle)


    triangle.penup()
    triangle.forward(75) 
    triangle.pendown()
    triangle.forward(75)
    draw_triangleSS(triangle)

    ''' #要畫 左邊跟右邊
    triangle.penup()
    triangle.backward(37.5)
    triangle.left(120)
    triangle.forward(37.5)    
    triangle.pendown()
    draw_triangleSSS(triangle)'''
   
    ''' triangle.penup()
    triangle.forward(150)
    triangle.left(120)
    triangle.backward(150)    
    triangle.pendown()
    draw_triangleSS(triangle)'''


    '''triangle.penup()
    triangle.forward(37.5)
    triangle.left(120)
    triangle.backward(37.5)    
    triangle.pendown()
    draw_triangleSSS(triangle)'''

    
    
    #window.exitonclick()
    
draw_square()


