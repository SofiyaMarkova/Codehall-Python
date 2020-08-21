print("Welcome to Wild Waterworld!")

age = int(input('enter your age'))

def calculateTicketPrice(age):
	if age > 0 and age <= 8:
  		return 15

	elif age >= 9 and age <= 12 or age > 65:
  		return 30

	elif age >=13 and age <= 18:
  		return 35
  
	elif age >= 19 and age <= 65:
  		return 40		  
	else:
  		print("No Entry")
  
		
price = calculateTicketPrice(age)

print('ticket price is $', price)


#psedo code
'''
age_1 = (1-8)
age_2 = (9-12)
age_3 = (13-18)
age_4 = (19-65)
age_5 = (65-100)
'''


  
  
