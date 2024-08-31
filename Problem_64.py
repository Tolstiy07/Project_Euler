'''
Задача 64
Квадратные корни с нечетным периодом
Любой квадратный корень является периодическим, если записать его в виде непрерывных дробей
 в следующей форме:

√N = a0 +   
1
    a1 +    
1
        a2 +    
1
            a3 + ...
К примеру, рассмотрим √23:

√23 = 4 + √23 — 4 = 4 +     
1
 = 4 +  
1
    
1
√23—4
    1 +     
√23 – 3
7
Продолжив это преобразование, мы получим следующее приближение:

√23 = 4 +   
1
    1 + 
1
        3 + 
1
            1 + 
1
                8 + ...
Этот процесс можно обобщить в следующем виде:

a0 = 4,     
1
√23—4
 =  
√23+4
7
 = 1 +  
√23—3
7
a1 = 1,     
7
√23—3
 =  
7(√23+3)
14
 = 3 +  
√23—3
2
a2 = 3,     
2
√23—3
 =  
2(√23+3)
14
 = 1 +  
√23—4
7
a3 = 1,     
7
√23—4
 =  
7(√23+4)
7
 = 8 +  √23—4
a4 = 8,     
1
√23—4
 =  
√23+4
7
 = 1 +  
√23—3
7
a5 = 1,     
7
√23—3
 =  
7(√23+3)
14
 = 3 +  
√23—3
2
a6 = 3,     
2
√23—3
 =  
2(√23+3)
14
 = 1 +  
√23—4
7
a7 = 1,     
7
√23—4
 =  
7(√23+4)
7
 = 8 +  √23—4
Нетрудно заметить, что последовательность является периодической. 
Для краткости введем обозначение √23 = [4;(1,3,1,8)], 
чтобы показать что блок (1,3,1,8) бесконечно повторяется.

Первые десять представлений непрерывных дробей (иррациональных) квадратных корней:

√2=[1;(2)], период = 1
√3=[1;(1,2)], период = 2
√5=[2;(4)], период = 1
√6=[2;(2,4)], период = 2
√7=[2;(1,1,1,4)], период = 4
√8=[2;(1,4)], период = 2
√10=[3;(6)], период = 1
√11=[3;(3,6)], период = 2
√12= [3;(2,6)], период = 2
√13=[3;(1,1,1,1,6)], период = 5


Период является нечетным у ровно четырех непрерывных дробей при N ≤ 13.

У скольких непрерывных дробей период является нечетным при N ≤ 10000?


'''
from time import time

def func(x):
    start = int(x**.5)
    if start**2 == x:
        return 0
    else:
        arr = [start,]
        a = start
        b = 0
        c = 1
        while arr[-1] != 2*start :
            
            b = c*a-b
            c = (x - b**2)//c
            a = int((start+b)/c)
            arr.append(a)
        return len(arr)-1


def main():
    start = time()
    res = 0
    for x in range(1,10001):
        if func(x)%2 != 0:
            res+=1
    print(f"{res} -непрерывных дробей период является нечетным при N ≤ 10000")

    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
