'''
Задача 20
Сумма цифр факториала
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
'''

num = 100
result = 1
result_2 = 0
for x in range(num,0,-1):
	result *= x
for x in str(result):
	result_2 += int(x)
print(result_2)