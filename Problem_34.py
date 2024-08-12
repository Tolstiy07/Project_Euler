'''
Задача 34
Факториалы цифр
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
'''
from time import time

start = time()

def func(x):
	summ = 0
	fact = 1
	for j in range(1,x+1):
		fact *= j
	summ += fact
	return summ

dic_fact= {}
for x in range(0,10):
	dic_fact[str(x)] = func(x)

num = 7 * func(9)

for x in range(10, num+1):
	if x == sum([dic_fact[n] for n in map(str,str(x))]):
		print(x)

end = time()

print(f"Program running time {round(end-start, 2)} sec.")