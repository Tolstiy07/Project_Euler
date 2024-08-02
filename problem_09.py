'''
Задача 9
Особая тройка Пифагора
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 52.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
'''

# def func(list_new):
# 	num = list_new[0]
# 	for x in list_new[1:]:
# 		if (num + x) in list_new:
# 			if int(num**0.5 + x**0.5 + (num + x)**0.5) == 1000:
# 				print(f"{num}+{x} = {num + x}")
# 				print(f"{int(num**0.5)} + {int(x**0.5)} + {int((num + x)**0.5)} = {int(num**0.5 + x**0.5 + (num + x)**0.5)}")
# 				return print(int(num**0.5) * int(x**0.5) * int((num + x)**0.5))
# 	if len(list_new) > 3:
# 		func(list_new[1:])
# 	else:
# 		return


# list_new = [x**2 for x in range(1,426)]

# print(func(list_new))


########################################

def compute():
	PERIMETR = 1000
	for a in range(1,PERIMETR+1):
		for b in range(a+1,PERIMETR+1):
			c = PERIMETR -a -b
			if a**2 + b**2 == c**2:
				return str(a * b *c)

print(compute())	
# 			