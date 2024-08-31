'''
Задача 62
Кубические перестановки
Можно найти перестановки куба 41063625 (3453), чтобы получить еще два 
куба: 56623104 (3843) и 66430125 (4053). К слову, 41063625 является наименьшим кубом, 
для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.



'''
from time import time

def main():
    start = time()
    min_ = 1
    while True:
        max_ = min_ * 10 -1
        min_8 = int(min_ **(1/3))
        max_8 = int(max_ **(1/3))
        number = []
        list_8=[]
        list_8_sort=[]
        numbers = []
        for x in range(min_8+1,max_8+1):
            number.append(x)
            list_8.append(x**3)
            num = (''.join(sorted(list(str(x**3))))) 
            list_8_sort.append(num)
            if list_8_sort.count(num) == 5:
                for i in range(len(list_8_sort)):
                    if list_8_sort[i] == list_8_sort[-1]:
                        numbers.append((number[i],list_8[i]))
                print(f"{numbers[0][1]} - наименьший куб, для которого ровно пять перестановок также являются кубами")
                print(f"Program running time {round(time() - start, 2)} sec.")
                exit()
        min_ = min_ *10

if __name__ == "__main__":
    main()
