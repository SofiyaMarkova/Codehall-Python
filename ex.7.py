def even(num):
	return num % 2 == 0

import turtle
t = turtle.Turtle()

t.speed(500)
for i in range(50):
	t.forward(100)
	t.right(95)
	if even(i):
		t.color('gold')
	else:
		t.color('blue')
		



