'''
Задача 52
Кратные из переставленных цифр Body:
Найдите такое наименьшее натуральное число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.

'''
from time import time

def main():
    start = time()

    x = 1
    while True:
        if sorted(list(str(2*x)))==sorted(list(str(3*x))):
            if sorted(list(str(2*x)))==sorted(list(str(4*x))):
                if sorted(list(str(2*x)))==sorted(list(str(5*x))):
                    if sorted(list(str(2*x)))==sorted(list(str(6*x))):
                        for i in range(2,7):
                            print(f"{i}x = {i*x} из {sorted(list(str(i*x)))}")
                        print(f"x = {x} - наименьшее натуральное число")
                        break
        x +=1

    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
