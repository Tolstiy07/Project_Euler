'''
Задача 10
Сложение простых чисел
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.


'''
# def func(num,list_n):
# 	for i in list_n:
# 		if num < i**2:
# 			break
# 		elif  num%i == 0:
# 			return False
# 	return True


# n = 2_000_000

# list_n = [2,]
# num = 3

# while num < n:
# 	if func(num,list_n):
# 		list_n.append(num)
		# print(num)
	# num += 1

# print(list_n)
# print(sum(list_n))
#142913828925
###################################################################


def list_prost_chisel(n):
	new_list = list(range(n))
	new_list[1] = 0
	for x in new_list[2:]:
		for j in range(x*2,len(new_list),x):
			new_list[j] = 0
	list_prost = list(set(new_list))
	list_prost.sort()
	return (list_prost[1:])

n = 2_000_000

new = list_prost_chisel(n)

print(sum(new))
