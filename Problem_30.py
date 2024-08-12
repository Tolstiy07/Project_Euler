'''
Задача 30
Пятые степени цифр
Удивительно, но существует только три числа, которые могут быть записаны 
в виде суммы четвертых степеней их цифр:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
1 = 14 не считается, так как это - не сумма.

Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
'''
from time import time

def main():
	start = time()

	res = 0
	k = 5
	dic = {}
	for x in range(0,10):
		dic[x**k]=str(x)
	list_=[x**k for x in range(0,10)]
	for a in list_:
		for b in list_:
			for c in list_:
				for d in list_:
					for e in list_:
						for f in list_:
							res_1 = a + b + c + d + e + f
							str_ = dic[a] + dic[b] + dic[c] + dic[d] + dic[e] + dic[f]
							if res_1 == int(str_):
								res += res_1
	print(res-1)
	end = time()
	print(f"Program running time - {end-start} sec.")

if __name__ == "__main__":
	main()

# #########################################

# def main():
# 	start = time()
# 	res = 0

# 	for i in range(10, 6*(9**5)):
# 		ss=0
# 		for x in str(i):

# 			ss += int(x)**5
# 		if ss == i:
# 			res += ss
# 	print(res)
# 	end = time()
# 	print(f"Program running time - {end-start} sec.")

# if __name__ == "__main__":
# 	main()
