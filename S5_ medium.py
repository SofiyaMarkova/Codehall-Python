saved = int(input('input much money you have saved'))
cost = int(input('input much money what you want to buy costs'))
hrpay = int(input('input much you earn per hour'))
hrwork = 0

def canIBuyThisYet(saved, cost, hrpay, hrwork):
	while True:
		if saved < cost:
			saved = saved + hrpay
			hrwork = hrwork + 1
		else:
			print('you need to work', hrwork, 'more hours')
			break
			
canIBuyThisYet(saved, cost, hrpay, hrwork) 