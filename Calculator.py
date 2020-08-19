print('Welcome to the calculator')

def calculate():
	operation = input('type +, -, *, / for what you want to do')
	
	number_1 = int(input('enter first number: '))
	print(number_1)
	number_2 = int(input('enter second number: '))
	print(number_2)
	
	if operation == '+':
		print('{} + {} = '.format(number_1, number_2))
		print(number_1 + number_2)		
	elif operation == '-':
		print('{} - {} = '.format(number_1, number_2))
		print(number_1 - number_2)
	elif operation == '*':
		print('{} * {} = '.format(number_1, number_2))
		print(number_1 * number_2)		
	elif operation == '/':
		print('{} / {} = '.format(number_1, number_2))
		print(number_1 / number_2)		
	else:
		print('invalid input')
		
def again():
	calc_again = input('type Y for Yes or N for No if want to compute againe')

	if calc_again.upper() == 'Y':
		calculate()
	
	elif calc_again.upper() == 'N':
		print('Goodbye')
	
	else:
		again()		
		
calculate()
again()