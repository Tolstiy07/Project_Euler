'''
Задача 60
Объединение пары в простое число
Простые числа 3, 7, 109 и 673 достаточно замечательны. Если взять любые два из них и 
объединить их в произвольном порядке, в результате всегда получится простое число. 
Например, взяв 7 и 109, получатся простые числа 7109 и 1097. Сумма этих четырех простых 
чисел, 792, представляет собой наименьшую сумму элементов множества из четырех простых 
чисел, обладающих данным свойством.

Найдите наименьшую сумму элементов множества из 5 простых чисел, для которых объединение 
любых двух даст новое простое число.


'''
from time import time
from sympy import nextprime, isprime


def func(x, y):
    res = (isprime(int(str(x) + str(y)))) and (isprime(int(str(y) + str(x))))
    return res


def func_2(x, y):
    res = True
    for i in range(len(x)):
        res = res and (isprime(int(str(x[i]) + str(y)))) and (isprime(int(str(y) + str(x[i]))))
    return res

def func_3(x_, z):
    y = nextprime(x_[0])
    while True:
        if func(x_[0], y):
            x_.append((x_[0], y))
            y = nextprime(y)
        else:
            y = nextprime(y)
        if y > z:
            return x_
def func_4(x_, z):
    x_2 = [x_[0], ]
    for i in range(1, len(x_)):
        y = nextprime(x_[i][1])
        while True:
            if func_2(x_[i], y):
                x_2.append((x_[i]+(y,)))
                y = nextprime(y)
            else:
                y = nextprime(y)
            if y > z:
                break
    return x_2


def main():
    start = time()

    z = 9000
    x_ = [2, ]
    while True:
        x_2 = func_4(func_4(func_4(func_3(x_, z),z),z),z)
        
        if len(x_2) >= 2:
            break
        x_ = [nextprime(x_2[0]), ]

    print(f"""{sum(x_2[1])} -наименьшая сумма элементов множества из 5 простых чисел {x_2[1]},
для которых объединение любых двух даст новое простое число. """)

    print(f"Program running time {round(time() - start, 2)} sec.")


if __name__ == "__main__":
    main()
