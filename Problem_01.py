'''
Задача 1
Числа, кратные 3 или 5
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
'''

def choise(num):
	for n in range(num):
		if n%3 == 0 or n%5 == 0:
			yield n

print(sum(choise(10)))
