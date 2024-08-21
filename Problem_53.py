'''
Задача 53
Комбинаторные выборки
Существует ровно десять способов выбора 3 
элементов из множества пяти {1, 2, 3, 4, 5}:

123, 124, 125, 134, 135, 145, 234, 235, 245, и 345

В комбинаторике для этого используется обозначение 5C3 = 10.

В общем случае,

nCr =   
n!
r!(n−r)!
, где r ≤ n, n! = n×(n−1)×...×3×2×1 и 0! = 1.
Это значение превышает один миллион, начиная с n = 23: 23C10 = 1144066.

Cколько значений (не обязательно различных)  nCr для 1 ≤ n ≤ 100 больше одного миллиона?



'''
from time import time
from math import factorial

def main():
    start = time()
    count = 0
    for n in range(1,101):
        for r in range(0,n+1):
            if ((factorial(n))//(factorial(n-r)*factorial(r)))>1000000:
                count += 1
    print(f"{count} - значений nCr для 1 ≤ n ≤ 100 больше одного миллиона") 

    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()

