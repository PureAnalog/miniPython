import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    n=1000
    a=3600/n
    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("turtle")
    brad.speed(100)
    for i in range(0, n):
        draw_square(brad)
        brad.right(a)
        brad.forward(2)
    
    window.exitonclick()

draw_circle()
