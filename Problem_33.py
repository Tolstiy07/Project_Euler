'''
Задача 33
Дроби, сократимые по цифрам
Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, 
будет ошибочно полагать, что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.

Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.

Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и 
содержат двухзначные числа как в числителе, так и в знаменателе.

Пусть произведение этих четырех дробей дано в виде несократимой дроби (числитель и 
знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби.
'''


result = 1
list_1 = [x for x in range(10,100) if x%10 != 0]
list_2 = []
for x in list_1:
	str_ = str(x)
	if str_[0] != str_[1]:
		list_2.append(x)
index = 0
for x in list_2[:-1]:
	index +=1
	for y in list_2[index:]:
		res = x/y
		str_1 = str(x)
		str_2 = str(y)
		if str_1[0] == str_2[0]:
			if res == int(str_1[1])/int(str_2[1]):
				result *= res
				print(f"{x}/{y} and {str_1[1]}/{str_2[1]} result {x/y}")
		elif str_1[0] == str_2[1]:
			if res == int(str_1[1])/int(str_2[0]):
				result *= res
				print(f"{x}/{y} and {str_1[1]}/{str_2[0]} result {x/y}")
		elif str_1[1] == str_2[0]:
			if res == int(str_1[0])/int(str_2[1]):
				result *= res
				print(f"{x}/{y} and {str_1[0]}/{str_2[1]} result {x/y}")
		elif str_1[1] == str_2[1]:
			if res == int(str_1[1])/int(str_2[1]):
				result *= res
				print(f"{x}/{y} and {str_1[1]}/{str_2[1]} result {x/y}")
print(round(result,3))