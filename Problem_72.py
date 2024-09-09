'''

Задача 72
Счет дробей
Рассмотрим дробь n/d, где n и d являются натуральными числами. Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.

Если перечислить множество сокращенных правильных дробей для d ≤ 8 в порядке возрастания их значений, получим:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

Нетрудно заметить, что данное множество состоит из 21 элемента.

Из скольки элементов будет состоять множество сокращенных правильных дробей для d ≤ 1 000 000?

'''
from time import time

def main():
    start = time()


    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
