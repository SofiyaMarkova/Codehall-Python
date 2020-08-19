import turtle

t = turtle.Turtle()
t.speed(10)
t.color('white')

for i in range(300):
	t.forward(2*i)
	t.right(90)