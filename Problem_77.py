'''
Задача 77
Простые суммы
Число 10 можно записать в виде суммы простых чисел ровно пятью различными способами:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

Какое наименьшее число можно записать в виде суммы простых чисел по крайней мере пятью тысячами различных способов?


'''
from time import time

def main():
    start = time()


    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
