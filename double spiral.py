import turtle
t = turtle.Turtle()
t.speed(50)
def draw_never_ending_square():
    for i in range(50):
        t.forward(2*i)
        t.right(90)

draw_never_ending_square()
t.forward(48)
t.right(90)
t.penup()
t.forward(52)
t.pendown()
t.left(45)
draw_never_ending_square()
