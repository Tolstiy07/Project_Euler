'''
Задача 68
Магическое пятиугольное кольцо
Рассмотрим следующее "магическое" треугольное кольцо, 
заполненное числами от 1 до 6, с суммой на каждой линии равной 9.


Проходя по направлению часовой стрелки, начав с группы с наименьшим внешним узлом 
(в данном примере: 4,3,2), каждое решение можно описать единственным образом. 
К примеру, вышеуказанное решение можно описать множеством: 4,3,2; 6,2,1; 5,1,3.

Существует возможность заполнить кольцо с четырьмя различными суммами на линиях: 9, 10, 11 и 12. 
Всего существует восемь решений.

Сумма   Множество решений
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3
10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5
11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6
12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6
Объединяя элементы каждой группы, можно образовать 9-тизначную строку. 
Максимальное значение такой строки для треугольного кольца составляет 432621513.

Используя числа от 1 до 10, в зависимости от расположения, можно образовать 16-тизначные 
и 17-тизначные строки. Каково максимальное значение 16-тизначной строки для "магического" пятиугольного кольца?




'''
from time import time
from itertools import combinations


def func(list_s1, n):
    return [x for x in list_s1 if sum(x) == n]


def func_2(i):
    s = []
    for x in i:
        for j in x:
            s.append(j)
    s_1 = list(set(s))
    one = 0
    one_l = []
    duble = 0
    for x in s_1:
        if s.count(x) == 2:
            duble += 1
        elif s.count(x) == 1:
            one += 1
            one_l.append(x)

    if duble == 5 and one == 5:
        if func_4(i, one_l):
            return func_3(i, one_l)
        else:
            return False
    else:
        return False


def func_3(i, one):
    k = min(one)
    num = str(k)
    i = list(i)
    for x in i:
        if k in x:
            x_2 = list(x)
            x_2.remove(k)
            if x_2[0] < x_2[1]:
                num += str(x_2[1]) + str(x_2[0])
            else:
                num += str(x_2[0]) + str(x_2[1])
            i.remove(x)
    ras = 0
    while ras < 4:
        z = int(num[-1])
        if z == 0:
            z = 10
        for x in i:
            if z in x:
                for j in x:
                    if j in one:
                        num += str(j) + str(z)
                        break
                for l in x:
                    if l != j and l != z:
                        num += str(l)
                        break
                i.remove(x)
        ras += 1
    return int(num)


def func_4(i, one):
    i = list(i)
    res = 0
    for x in one:
        for j in i:
            if x in j:
                i.remove(j)
                res += 1
    if res == 5:
        return True
    else:
        return False


def main():
    start = time()

    list_num = [x for x in range(1, 11)]

    list_s1 = [x for x in combinations(list_num, 3)]
    list_s = [sum(x) for x in combinations(list_num, 3)]
    many_2 = [x for x in list(set(list_s)) if list_s.count(x) > 4]

    f = 0
    arr = []
    for x in many_2:
        group = func(list_s1, x)
        group_s1 = [x for x in combinations(group, 5)]

        for i in group_s1:
            res = func_2(i)
            if res != False and len(str(res)) == 16:
                arr.append(res)
    print(f"{max(arr)} - максимальное значение 16-тизначной строки для \"магического\" пятиугольного кольца")

    print(f"Program running time {round(time() - start, 2)} sec.")


if __name__ == "__main__":
    main()
