'''
Задача 50
Сумма последовательных простых чисел
Простое число 41 можно записать в виде суммы шести последовательных простых чисел:

41 = 2 + 3 + 5 + 7 + 11 + 13
Это - самая длинная сумма последовательных простых чисел, в результате которой получается 
простое число меньше одной сотни.

Самая длинная сумма последовательных простых чисел, в результате которой получается простое 
число меньше одной тысячи, содержит 21 слагаемое и равна 953.

Какое из простых чисел меньше одного миллиона можно записать в виде суммы наибольшего 
количества последовательных простых чисел?


'''
from time import time


def main():
    start = time()

    list_num = [x for x in range(1_000_000)]
    list_num[1] = 0
    arr_simple = []
    x = 0
    while x < len(list_num):
        if list_num[x] != 0:
            arr_simple.append(x)
            for i in range(x, len(list_num), x):
                list_num[i] = 0
        x += 1

    k = 0
    result = 0

    len_simple = len(arr_simple)

    for i in range(len_simple):
        for j in range(i + k, len_simple):
            sol = sum(arr_simple[i:j])
            if sol < 1000000 and sol in arr_simple and sol > result:
                k = j - i
                new_x = (arr_simple[i:j])
                result = sol
            elif sol > 1000000:
                break

    print(f"{result} - сумма наибольшего количества последовательных простых чисел меньше одного миллиона")

    print(f"Program running time {round(time() - start, 2)} sec.")


if __name__ == "__main__":
    main()
