'''
Задача 44
Пятиугольные числа
Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48, 
не является пятиугольным числом.

Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность 
являются пятиугольными числами и значение D = |Pk − Pj| минимально, и дайте 
значение D в качестве ответа.
'''
from time import time

def formul(x):
	return (x*(3*x-1))/2

def change(x):
	if (((24*x + 1)**0.5) + 1)%6 == 0:
		return True
	return False

def main():
    start = time()
    flag = True
    i = 1
    while flag:
    	for x in range(1,i):
    		a = formul(i)
    		b = formul(x)
    		if change(b+a) and change(abs(b-a)):
    			flag = False
    			break
    	i +=1


    print(f"""Пара пятиугольных чисел Pk={int(b)} и Pj={int(a)}, для которых сумма и разность 
являются пятиугольными числами и значение D = |Pk − Pj| = {abs(b-a)}  минимально.""")

    print(f"Program running time {round(time() - start, 2)} sec.")


if __name__ == "__main__":
    main()
