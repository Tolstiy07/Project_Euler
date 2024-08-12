'''
Задача 31
Суммы монет
В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое количество монет?
'''
from time import time

start = time()

def func(amount,coins):
	if amount == 0:
		return 1
	elif amount<0 or len(coins)<1:
		return 0
	else:
		coin = coins[0]
		rest = coins[1:]
		return func(amount-coin,coins) + func(amount,rest)




def main():
	coins = [200, 100, 50, 20, 10, 5, 2, 1]
	amount = 200
	print(func(amount,coins))

main()


end = time()

print(f"Program running time {round(end-start,2)} sec.")