'''
Задача 61
Цикличные фигурные числа
К фигурным (многоугольным) числам относятся треугольные, квадратные, пятиугольные, шестиугольные,
семиугольные и восьмиугольные числа, которые расчитываются по следующим формулам:

Треугольные         P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
Квадратные          P4,n=n2             1, 4, 9, 16, 25, ...
Пятиугольные        P5,n=n(3n−1)/2      1, 5, 12, 22, 35, ...
Шестиугольные       P6,n=n(2n−1)        1, 6, 15, 28, 45, ...
Семиугольные        P7,n=n(5n−3)/2      1, 7, 18, 34, 55, ...
Восьмиугольные      P8,n=n(3n−2)        1, 8, 21, 40, 65, ...
Упорядоченное множество из трех четырехзначных чисел: 8128, 2882, 8281, обладает тремя интересными 
свойствами

Множество является цикличным: последние две цифры каждого числа являются первыми 
двумя цифрами следующего (включая последнее и первое числа).
Каждый тип многоугольника — треугольник (P3,127=8128), квадрат (P4,91=8281) и 
пятиугольник (P5,44=2882) — представлены различными числами данного множества.
Это — единственное множество четырехзначных чисел, обладающее указанными свойствами.

Найдите сумму элементов единственного упорядоченного множества из шести 
цикличных четырехзначных чисел, в котором каждый тип 
многоугольников — треугольник, квадрат, пятиугольник, шестиугольник, семиугольник и восьмиугольник — 
представлены различными числами этого множества.

'''
from time import time

def list_3(x,y):
    max_ = int((((8*x+1)**.5)-1)/2)
    min_ = int((((8*y+1)**.5)-1)/2)
    return [(3,int((x*(x+1))/2))  for x in range(min_+1,max_+1)]

def list_4(x,y):
    max_ = int((x)**.5)
    min_ = int((y)**.5)
    return [(4,int(x**2))  for x in range(min_+1,max_+1)]

def list_5(x,y):
    max_ = int((((24*x+1)**.5)+1)/6)
    min_ = int((((24*y+1)**.5)+1)/6)
    return [(5,int(x*(3*x-1)/2))  for x in range(min_+1,max_+1)]

def list_6(x,y):
    max_ = int((((8*x+1)**.5)+1)/4)
    min_ = int((((8*y+1)**.5)+1)/4)
    return [(6,int(x*(2*x-1)))  for x in range(min_+1,max_+1)]

def list_7(x,y):
    max_ = int(63)
    min_ = int(20)
    return [(7,int(x*(5*x-3)/2))  for x in range(min_+1,max_+1)]

def list_8(x,y):
    max_ = int((((3*x+1)**.5)+1)/3)
    min_ = int((((3*y+1)**.5)+1)/3)
    return [(8,int(x*(3*x - 2)))  for x in range(min_+1,max_+1)]


def main():
    start = time()

    x = 9999
    y = 1000

    new_list = list_3(x,y) + list_4(x,y) + list_5(x,y) + list_6(x,y) + list_7(x,y) + list_8(x,y)


    arr=[]
    for x in new_list:
        for j in new_list:
            if str(x[1])[:2] == str(j[1])[2:] and (x[0])!=(j[0]):
                arr.append((j,x))

    arr_1 =[]
    for i in arr:
        for j in new_list:
            if (str(i[0][1])[:2] == str(j[1])[2:] and
                (i[0][0])!=(j[0]) and 
                (i[1][0])!=(j[0])):
                arr_1.append((j,)+i)


    arr =[]
    for i in arr_1:
        for j in new_list:
            if (str(i[0][1])[:2] == str(j[1])[2:] and
                 (i[0][0])!=(j[0]) and
                 (i[1][0])!=(j[0]) and
                 (i[2][0])!=(j[0])):
                arr.append((j,)+i)

    arr_1 =[]
    for i in arr:
        for j in new_list:
            if (str(i[0][1])[:2] == str(j[1])[2:] and
                (i[0][0])!=(j[0]) and 
                (i[1][0])!=(j[0]) and
                (i[2][0])!=(j[0]) and
                (i[3][0])!=(j[0])):
                arr_1.append((j,)+i)

    arr =[]
    for i in arr_1:
        for j in new_list:
            if (str(i[0][1])[:2] == str(j[1])[2:] and
                 (i[0][0])!=(j[0]) and
                 (i[1][0])!=(j[0]) and
                 (i[2][0])!=(j[0]) and
                 (i[3][0])!=(j[0]) and
                 (i[4][0])!=(j[0]) and
                 str(i[4][1])[2:] == str(j[1])[:2]):
                arr.append((j,)+i)
             
    res = []
    dic = {}
    for j in arr[0]:
        res.append(j[1])
        dic[j[0]] = j[1]     
    print(f"""{sum(res)} - сумму элементов единственного упорядоченного множества {res} из шести 
цикличных четырехзначных чисел, в котором каждый тип многоугольников — треугольник ({dic[3]}), квадрат ({dic[4]}), 
пятиугольник ({dic[5]}), шестиугольник ({dic[6]}), семиугольник ({dic[7]}) и восьмиугольник ({dic[8]}) 
— представлены различными числами этого множества.""")


    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
