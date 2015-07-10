import turtle



def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("turtle")
    brad.speed(2)
    draw_square(brad)
   
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.circle(200)

    phil =turtle.Turtle()
    phil.shape("triangle")
    phil.color("pink")

    current_loop=0
    total_loop = 3

    while( current_loop < total_loop):
        phil.forward(100)
        phil.left(120)
        current_loop =current_loop+1
   
  
    window.exitonclick()

draw_art()
