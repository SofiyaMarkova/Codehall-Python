print("Welcome to Wild Waterworld!")

age = int(input('enter your age'))

def calculateTicketPrice(age):
	if age > 0 and age <= 8:
  		print('the ticket price is $15')

	elif age >= 9 and age <= 12 or age > 65:
  		print('the ticket price is $30')

	elif age >=13 and age <= 18:
  		print('the ticket price is $35')
  
	elif age >= 19 and age <= 65:
  		print('the ticket price is $40')	  
	
	else:
  		print("invalid input")
		
calculateTicketPrice(age)

#psedo code
'''
15 = (1-8)
30 = (9-12)
35 = (13-18)
40 = (19-65)
30 = (65-100)
'''


  
  
