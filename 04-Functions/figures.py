import turtle

length=int(input())

def draw_square(length):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
