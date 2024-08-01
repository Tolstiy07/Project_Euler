'''
Задача 4
Наибольшее произведение-палиндром
Число-палиндром с обеих сторон (справа налево и слева направо) 
читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел
'''

num_1, num_2 = 999, 999


def proiz(x, y):  # произведение
    return x * y


def chet(x):
    return len(str(x)) % 2 == 0


def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])


num_1, num_2 = 999, 999

while True:
    sum_num = proiz(num_1, num_2)

    if chet(sum_num):
        if palindrom(str(sum_num)):
            print(f"Все: {num_1} * {num_2} = {sum_num}")
            break
    if num_1 == num_2:
        num_1 -= 1
    else:
        num_2 -= 1
