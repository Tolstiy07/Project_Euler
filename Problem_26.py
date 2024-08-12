'''
Задача 26
Обратные циклы
Единичная дробь имеет 1 в числителе. 
Десятичные представления единичных дробей со знаменателями 
от 2 до 10 даны ниже:

1/2	=	0.5
1/3	=	0.(3)
1/4	=	0.25
1/5	=	0.2
1/6	=	0.1(6)
1/7	=	0.(142857)
1/8	=	0.125
1/9	=	0.(1)
1/10	=	0.1

Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. 
Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую 
длинную повторяющуюся последовательность цифр.

'''
from time import time

start = time()


def traditional():
    start = 2
    limit = 1000
    max_num = 1
    max_cycle = 1

    for d in range(start, limit + 1):
        n = 1
        while n < d:
            x = 10 ** n - 1
            if x % d == 0:
                break
            n += 1
        if n != d:
            if n > max_cycle:
                max_cycle = n
                max_num = d

    return max_num, max_cycle


print(traditional())

finish = time()

print(f"Время работы программы {finish-start} секунд")