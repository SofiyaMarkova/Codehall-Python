from random import random
from random import randint

print('1: rock, 2: paper, 3: scissors')

player = int(input('input the number for rock, paper, or scissors'))

computer = randint(1,3)

print('you said', player)
print('the computer said', computer)

if computer == player:
	print('tie')
	
elif computer == 3 and player == 1:
		print('you win')
	
elif computer == 3 and player == 2:	
		print('you lose')

elif computer == 2 and player == 1:
		print('you lose')

elif computer == 2 and player == 3:
		print('you win')
		
elif computer == 1 and player == 2:
		print('you win')

elif computer == 1 and player == 3:
		print('you lose')
		
	 