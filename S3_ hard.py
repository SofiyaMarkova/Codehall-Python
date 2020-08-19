num = int(input('input number to check if it is prime'))
i = 2

while True:
	if num % i == 0:
		print('not prime')
		break	
	elif num == i + 1:
		print('prime')
		break	
	else:
		i += 1