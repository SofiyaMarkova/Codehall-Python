import turtle

t = turtle.Turtle()

#worse version
t.forward(2*1)
t.right(90)
t.forward(2*2)
t.right(90)
t.forward(2*3)
t.right(90)
t.forward(2*4)
t.right(90)
t.forward(2*5)
t.right(90)
t.forward(2*6)
t.right(90)
t.forward(2*7)
t.right(90)

#better version
#0,7
for i in range(0,7):
	t.forward(2 * i)
	t.right(90)
