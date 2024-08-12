'''
Задача 35
Круговые простые числа
Число 197 называется круговым простым числом, 
потому что все перестановки его цифр с конца в начало 
являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 
100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?


'''
from time import time

start = time()

number = 1_000_000

list_num = [x for x in range(number + 1)]
list_num[1] = 0
simple_list = []
new_simple = []

index = 2
while index <= number:
    if list_num[index] != 0:
        simple_list.append(index)
        for num in range(index, number, index):
            list_num[num] = 0
    index += 1

simple_list_2 = [2, ]
for x in simple_list[1:]:
    str_ = list(str(x))
    if '0' not in str_:
        if '2' not in str_:
            if '4' not in str_:
                if '6' not in str_:
                    if '8' not in str_:
                        simple_list_2.append(x)

for x in simple_list_2:
    if x not in new_simple:
        arr = []
        str_x = str(x)
        num0 = len(str_x)
        for x in range(num0):
            str_x = str_x[1:] + str_x[0]
            if int(str_x) in simple_list_2:
                arr.append(int(str_x))
            else:
                break
        if num0 == len(arr):
            for x in arr:
                if x not in new_simple:
                    new_simple.append(x)

print((new_simple))
print(f"Cуществует {len(new_simple)} круговых простых чисел меньше миллиона")

end= time()
print(f'Program running time {round(end-start,2)} sec.')