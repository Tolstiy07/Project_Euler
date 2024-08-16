'''

Задача 47
Различные простые множители
Первые два последовательные числа, каждое из которых имеет 
два отличных друг от друга простых множителя:

14 = 2 × 7
15 = 3 × 5

Первые три последовательные числа, каждое из которых имеет 
три отличных друг от друга простых множителя:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Найдите первые четыре последовательных числа, каждое из которых 
имеет четыре отличных друг от друга простых множителя. Каким будет первое число?



'''
from time import time


def func(x):
    if x == 2:
        return True
    if x <= 1 or x % 2 == 0:
        return False
    for i in range(3, int(x ** .5) + 1, 2):
        if x % i == 0:
            return False
    return True


def func_2(x):
    k = 2
    arr = []
    while k < x ** .5:
        if x % k == 0 and func(k):
            x = int(x / k)
            arr.append(k)
        k += 1
    if not func(x) and len(arr) >= 3:
        for j in range(len(arr)):
            if x % arr[j] == 0 and func(int(x / arr[j])):
                arr.append(int(x / arr[j]))
                arr[j] = arr[j] ** 2
                return (arr)

    arr.append(x)
    return (arr)


def main():
    start = time()

    k = 2 * 3 * 5 * 7

    while True:
        if len(func_2(k)) >= 4:
            if len(func_2(k + 1)) >= 4:
                if len(func_2(k + 2)) >= 4:
                    if len(func_2(k + 3)) >= 4:
                        print(func_2(k))
                        print(func_2(k + 1))
                        print(func_2(k + 2))
                        print(func_2(k + 3))
                        print(f"""{k} - первое число первых четырех последовательных чисел,
каждое из которых имеет четыре отличных друг от друга простых множителя.""")
                        break
        k += 1

    print(f"Program running time {round(time() - start, 2)} sec.")


if __name__ == "__main__":
    main()
