num = int(input('input the number to check if it is prime'))

#1 is not a prime or composite number (so start check at 2)

if num > 1:
	for i in range(2,num):
		if (num % i == 0):
			print(num,'not prime') 
			break
#using the other notation for printing. this one gives a space too
		else:
			print(num, 'is prime')
	  
elif num == 0 or num == 1: #because 1 is not prime or composite
	print(num,'not prime or composite')
else:
	print(num, 'is prime')