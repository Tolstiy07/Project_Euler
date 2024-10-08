'''
Задача 27
Квадратичные простые числа
Эйлер опубликовал свою замечательную квадратичную формулу:

n2+n+41
Оказалось, что согласно данной формуле можно получить 40 простых чисел, последовательно подставляя 
значения 0≤n≤39
. Однако, при n=40
, 402+40+41=40(40+1)+41
 делится на 41 без остатка, и, очевидно, при n=41,412+41+41
 делится на 41 без остатка.

При помощи компьютеров была найдена невероятная формула n2−79n+1601
, согласно которой можно получить 80 простых чисел для последовательных значений n
 от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:

n2+an+b
, где |a|<1000
 и |b|≤1000


где |n|
 является модулем (абсолютным значением) n
.
К примеру, |11|=11
 и |−4|=4
Найдите произведение коэффициентов a
 и b
 квадратичного выражения, согласно которому можно получить максимальное 
  простых чисел для последовательных значений n
, начиная со значения n=0
.
'''
from time import time

start = time()

def func(n): # функция проверки числа простое или нет
    res = False
    if n == 2:
        return True

    for x in range(2,n):
        if n%x == 0:
            res = False
            break 
        else:
            res = True

    return res

list_1 = [x for x in range(1000) if func(x)] #создание списка простых чисел от 0 до 1000
list_2 = list_1.copy()


max_ = 0
mij = 0

for a in list_1:
    for b in list_1:
        k = 0

        while True:
            res = k**2 +a*k + b
            if res not in list_2:
                if func(res):
                    list_2.append(res)
                else:
                    if k-1 > max_:
                        max_ = k-1
                        mij = a*b
                    break 
            k += 1
        while True:
            res = k**2 - a*k + b
            if res not in list_2:
                if func(res) and res > 0:
                    list_2.append(res)
                else:
                    if k-1 > max_:
                        max_ = k-1
                        mij = -1 *a*b
                    break 
            k += 1

print(f"{mij} - произведение коэффициентов a и b квадратичного выражения,")
print("согласно которому можно получить максимальное простых чисел для последовательных")
print("значений n, начиная со значения n=0")

end = time()
print(f"Время работы программы {round(end-start,2)} секунд")