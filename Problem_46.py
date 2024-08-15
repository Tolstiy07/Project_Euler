'''
Задача 46
Другая проблема Гольдбаха
Кристиан Гольдбах показал, что любое нечетное составное число 
можно записать в виде суммы простого числа и удвоенного квадрата.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

Оказалось, что данная гипотеза неверна.

Каково наименьшее нечетное составное число, которое нельзя 
записать в виде суммы простого числа и удвоенного квадрата?

'''

from time import time


def func(x):
    if x <= 1 or x % 2 == 0:
        return False
    elif x == 2:
        return True
    for i in range(3, (int(x ** .5)) + 1, 2):
        if x % i == 0:
            return False
    return True


def main():
    start = time()
    k = 9
    while True:
        if not func(k):
            k_2 = 1
            result = 2
            flag = True
            while result > 1:
                result = k - 2 * k_2 ** 2
                if func(result):
                    flag = False
                    break
                k_2 += 1
            if flag:
                print(f"""{k} - наименьшее нечетное составное число, которое нельзя 
записать в виде суммы простого числа и удвоенного квадрата""")
                break
        k += 2

    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
