'''
Задача 3
Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

num = 600851475143
count = 2

while True:
	if num%count == 0:
		num /=count
		if num == 1:
			print(count)
			break
	count += 1