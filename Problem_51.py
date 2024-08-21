'''
Задача 51
Замена цифр в простом числе
Меняя первую цифру числа *3 (двузначного числа, заканчивающегося цифрой 3), 
оказывается, что шесть из девяти возможных значений - 13, 23, 43, 53, 73 и 83 - 
являются простыми числами.

При замене третьей и четвертой цифры числа 56**3 одинаковыми цифрами, 
получаются десять чисел, из которых семь - простые: 56003, 56113, 56333, 56443, 56663, 56773 и 56993. 
Число 56**3 является наименьшим числом, подставление цифр в которое дает именно семь простых чисел. 
Соответственно, число 56003, будучи первым из полученных простых чисел, является наименьшим простым 
числом, обладающим указанным свойством.

Найдите наименьшее простое число, которое является одним из восьми простых чисел, полученных
заменой части цифр (не обязательно соседних) одинаковыми цифрами.

'''
from time import time
from itertools import product


def func_1(x):
    arr = [x for x in range(x)]
    arr[1] = 0
    new_arr = []
    k = 2
    while k < len(arr):
        if arr[k] != 0:
            new_arr.append(k)
            for i in range(k, len(arr), k):
                arr[i] = 0
        k += 1
    return (new_arr)


def func_2(x):
    list_str = [i for i in str(x)]
    list_bool = list(product((True, False), repeat=len(list_str)))[1:-1]
    for p in list_bool:
        new_str = ""
        for i, res in enumerate(p):
            if res:
                new_str += list_str[i]
            else:
                new_str += "X"
        yield [int(new_str.replace('X', str(n))) for n in range(10)]


def func_3(x):
    if x == 2:
        return True
    elif x <= 1 or x % 2 == 0:
        return False
    for i in range(3, int(x ** .5) + 1, 2):
        if x % i == 0:
            return False
    return True


def main():
    start = time()

    for x in func_1(1_000_000):
        for y in func_2(x):
            new_list_2 = [x_2 for x_2 in y if func_3(x_2) and len(str(x)) == len(str(x_2))]
            if len(new_list_2) == 8 and x in new_list_2:
                print(f"""{x} - наименьшее простое число, которое является одним из восьми простых чисел, полученных
заменой части цифр (не обязательно соседних) одинаковыми цифрами.""")
                print(f"Program running time {round(time() - start, 2)} sec.")
                return


if __name__ == "__main__":
    main()
