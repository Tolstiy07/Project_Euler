'''
Задача 49
Перестановки простых чисел
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330,
необычна в двух отношениях: (1) каждый из трех членов является простым числом, (2) все 
три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных 
простых чисел, демонстрирующих это свойство. Однако, существует еще одна четырехзначная 
возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?
'''

from time import time


def func(x):
    if x == 2:
        return True
    elif x <= 1 or x % 2 == 0:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True


def main():
    start = time()
    arr = []
    arr_not = ['1', '4', '7', '8']
    for n in range(1000, 10000):
        if func(n):
            arr.append(n)

    for x in range(len(arr)):
        k = x + 1
        while k < 651:
            arr_1 = list(str(arr[x]))
            arr_2 = list(str(arr[k]))
            arr_3 = list(str(arr[k] - arr[x] + arr[k]))
            if sorted(arr_1) == sorted(arr_2) and sorted(arr_2) == sorted(arr_3) and sorted(arr_1) != arr_not:
                if (arr[k] - arr[x] + arr[k]) in arr:
                    print(''.join(arr_1 + arr_2 + arr_3),
                          """ 12-значное число образуется, если объединить три члена этой прогрессии""")
                    print(f"Program running time {round(time() - start, 2)} sec.")
                    exit()
            k += 1


if __name__ == "__main__":
    main()
