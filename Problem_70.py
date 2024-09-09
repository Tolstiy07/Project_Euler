'''

Задача 70
Перестановка функции Эйлера
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения 
количества чисел, меньших n, которые взаимно просты с n. 
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9) = 6.
Число 1 считается взаимно простым для любого положительного числа, так что φ(1) = 1.

Интересно, что φ(87109) = 79180, и, как можно заметить, 87109 является перестановкой 79180.

Найдите такое значение n, 1 < n < 107, при котором φ(n) является перестановкой n, 
а отношение n/φ(n) является минимальным.

'''
from time import time

def primes(n):
    list_1 = [x for x in range(n)]
    list_1[1] = 0
    list_2 = []
    ind = 2
    while ind < len(list_1):
        if list_1[ind] != 0:
            list_2.append(ind)
            for x in range(ind, len(list_1), ind):
               list_1[x] = 0
        ind +=1
    return(list_2)


def main():
    start = time()
    n = 4_000
    sotn = 100
    list_primes = primes(n)
    for x in list_primes:
        for y in list_primes:
            if x*y < 1e7:
                new_res_1 = x*y
                new_res_2 = (x-1)*(y-1)
                if ((x*y)/((x-1)*(y-1)) < sotn and
                    sorted(str(new_res_1))==sorted(str(new_res_2))):
                    sotn = ((x*y)/((x-1)*(y-1)))
                    res_1 = new_res_1
                    res_2 = new_res_2
    print(f"""{res_1} - значение n, при котором φ(n) является перестановкой n, 
а отношение n/φ(n) является минимальным.""")





    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
