'''
Задача 80
Цифровое представление квадратных корней
Как известно, если квадратный корень натурального числа не является целым числом, то он является иррациональным числом. Разложение таких квадратных корней на десятичные дроби бесконечно и не имеет никакой повторяющейся последовательности.

Квадратный корень из двух равен 1.41421356237309504880..., а сумма его первых ста цифр в десятичном представлении равна 475.

Найдите общую сумму первых ста цифр всех иррациональных квадратных корней среди первых ста натуральных чисел.




'''
from time import time

def main():
    start = time()


    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
