list = []

#to populate list well
for i in range(20):
	list.append(i+1)
print(list)

#getting the multiplication table for up to 19
for x in range(1,len(list)):
	list2 = []
	for i in list:
		list2.append(i*x)
	print(list2)