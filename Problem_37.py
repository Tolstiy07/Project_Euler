'''
Задача 37
Укорачиваемые простые числа
Число 3797 обладает интересным свойством. 
Будучи само по себе простым числом, из него можно последовательно выбрасывать 
цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7. 
Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать 
цифры как справа налево, так и слева направо, но числа при этом остаются простыми.

ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
'''
from time import time

start = time()


def right_func(x, simple):
    str_x = str(x)
    for i in range(1, len(str_x)):
        if int(str_x[i:]) not in simple:
            return False
    return True


def left_func(x, simple):
    str_x = str(x)
    for i in range(1, len(str_x)):
        if int(str_x[:(-1 * i)]) not in simple:
            return False
    return True


result = 0

n = 1000000
number = [x for x in range(n + 1)]
simple_number = []
number[1] = 0
k = 2

while k <= n:
    if number[k] != 0:
        simple_number.append(number[k])
        for j in range(k, n + 1, k):
            number[j] = 0
    k += 1

simple_number_2 = []
for x in simple_number:
    if '4' not in list(str(x)):
        if '6' not in list(str(x)):
            if '8' not in list(str(x)):
                if '0' not in list(str(x)):
                    if '2' not in list(str(x))[1:]:
                        simple_number_2.append(x)

for x in simple_number[4:]:
    if right_func(x, simple_number_2) and left_func(x, simple_number_2):
        result += x

print(result)

end = time()
print(f"Program running time {round(end - start, 2)} sec.")
