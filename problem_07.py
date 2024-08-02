'''
Задача 7
10001-е простое число
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?
'''
def func(num,list_n):
	for i in list_n:
		if num < i**2:
			break
		elif  num%i == 0:
			return False
	return True


n = 10002
sum_n = 4
x = 7
list_n = [2, 3, 5, 7]

while n != sum_n:
	x +=2
	if func(x,list_n):
		sum_n += 1
		list_n.append(x)
print(list_n[-1])

########################################################################

# simple=[3]
# number=3
# count=3
# while count<=10001:
#     number+=2
#     print(number)
#     simpleNuber=True
#     for i in simple:
#         if number<i**2: #числа кратные i, начинают высчитывать с i(квадрат)
#             break
#         else:
#             if number%i==0:
#                 simpleNuber=False
#                 break
#     if simpleNuber==True:
#         simple.append(number)
#         count+=1
# print(simple[-1])




# for i in range(10,100):
# 	print(f"{list_n[i]} = {simple[i]}")

# for i in range(1,122):
# 	if 121%i == 0:
# 		print(i)