'''
Задача 5
Наименьшее кратное
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''


# def list_num(num):
#     return [x for x in range(2, num + 1)]


# def proverka(num_list, number):
#     for i in num_list:
#         if number % i != 0:
#             return False
#     return True


# list_d = list_num(20)

# number = 20

# while True:
#     if proverka(list_d, number):
#         print(f"{number} делится на все числа из списка")
#         break
#     else:
#         number += 20


###################################################

def resalt(suma, number, number_2, number_1):

	while number_2 >= 1:
		if suma%number_2 != 0:
			suma += number
		else:
			number_2 -= 1
			number = suma
	return f"Все числа до {number_1} делят {suma} на цело"

number_new  = 100

print (resalt(number_new, number_new, number_new-1, number_new))
