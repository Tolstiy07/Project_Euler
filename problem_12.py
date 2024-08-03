'''
Задача 12
Треугольное число с большим количеством делителей
Последовательность треугольных чисел образуется путем сложения натуральных чисел. К примеру, 7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?
'''

n = 2
summ_num = 1

while True:
	summ = 0
	k = ((summ_num**0.5))
	if summ_num%k == 0:
		summ = 1
	k = int(k)
	while k>1:
		k -= 1
		if summ_num%(k) == 0:
			summ +=2

	if summ >500:
		break
	summ_num += n
	n += 1
print(summ_num)