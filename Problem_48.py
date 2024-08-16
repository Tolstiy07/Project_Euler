'''
Задача 48
Собственные степени
Сумма 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.

'''
from time import time

def main():
    start = time()

    sum_num = 0
    for x in range(1,1000):
        sum_num += (x**x)
    print(f""".......{(str(sum_num))[-10:]} - последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.""")

    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
