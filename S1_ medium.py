#takes input, input function always a string. so change it to int()
radius = int(input('input the radius of the circle'))

#** is a power operator. here calculating area 
#used 3.14 to approximation
area = 3.14*radius**2

print('the area of the circle is about ' + str(area))
