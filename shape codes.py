import turtle

t = turtle.Turtle()

def square():
	t.pendown()
	for i in range(4):
		t.forward(100)
		t.left(90)
		
def circle():
	t.pendown()
	for i in range(360):
		t.forward(1)
		t.left(1)
		
def star():
	t.pendown()
	for i in range(5):
		t.forward(100)
		t.right(144)
		
