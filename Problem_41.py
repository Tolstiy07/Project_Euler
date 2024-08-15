'''
Задача 41
Пан-цифровое простое число
Будем считать n-значное число пан-цифровым, если каждая из цифр 
от 1 до n используется в нем ровно один раз. К примеру, 2143 
является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?
'''

from itertools import permutations
from time import time

def func(x):
	
	if x<=1 or x%2 == 0:
		return False
	elif x==2:
		return True
	for i in range(3,int(x**.5)+1,2):
		if x%i ==0:
			return False
	return True

def main():
	start = time()
	k=1
	while True:
		list_num = ['1', '2', '3', '4', '5', '6', '7','8','9','0']
		
		lst = list(permutations(list_num[:-1*k]))
		list_1 = []
		for x in lst:
			x =int(''.join(list(x)))
			if func(x):
				list_1.append(x)
		if len(list_1)>0:
			break
		k +=1
	print(f"{max(list_1)} - наибольшее n-значное пан-цифровое простое число.")

	print(f"Program running time {round(time()-start,2)} sec.")

if __name__ == "__main__":
	main()