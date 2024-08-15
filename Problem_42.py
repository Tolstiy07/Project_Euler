'''
Задача 42
Закодированные треугольные числа

n-й член последовательности треугольных чисел задается как tn = ½n(n+1). 
Таким образом, первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...


Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в алфавите, 
и складывая эти значения, мы получим числовое значение слова. 
Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t10. 
Если числовое значение слова является треугольным числом, то мы назовем 
это слово треугольным словом.

Используя words.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), 16 КБ 
текстовый файл, содержащий около двух тысяч часто используемых английских слов, 
определите, сколько в нем треугольных слов.
'''

from time import time


def check(x, alfa, triangle):
    res = 0
    arr = list(x)
    for x in arr:
        res += alfa[x]
    if res in triangle:
        return True
    else:
        return False


def triangle():
    arr = []
    for x in range(1, 25):
        arr.append(int(.5 * x * (x + 1)))
    return arr


def file():
    with open('words.txt', 'r') as f:
        list_1 = f.readline()
        list_1 = list_1.split('\",\"')
        list_1.insert(0, (list_1.pop(0))[1:])
        list_1.append((list_1.pop(-1))[:-1])
        return list_1


def alfabed():
    dic = {}
    k = 1
    for x in range(65, 65 + 26):
        dic[chr(x)] = k
        k += 1
    return dic


def main():
    start = time()

    triangl = triangle()
    words = file()
    alfa = alfabed()
    result = 0
    for x in words:
        if check(x, alfa, triangl):
            result += 1

    print(f"B words.txt {result} треугольных словa.")

    print(f"Program running time {round(time() - start, 2)} sec.")


if __name__ == "__main__":
    main()
