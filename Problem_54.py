'''
Задача 54
Покерные ставки
В карточной игре покер ставка состоит из пяти карт и 
оценивается от самой младшей до самой старшей в следующем порядке:

Старшая карта: Карта наибольшего достоинства.
Одна пара: Две карты одного достоинства.
Две пары: Две различные пары карт
Тройка: Три карты одного достоинства.
Стрейт: Все пять карт по порядку, любые масти.
Флаш: Все пять карт одной масти.
Фул-хаус: Три карты одного достоинства и одна пара карт.
Каре: Четыре карты одного достоинства.
Стрейт-флаш: Любые пять карт одной масти по порядку.
Роял-флаш: Десятка, валет, дама, король и туз одной масти.
Достоинство карт оценивается по порядку:
2, 3, 4, 5, 6, 7, 8, 9, 10, валет, дама, король, туз.

Если у двух игроков получились ставки одного порядка, 
то выигрывает тот, у кого карты старше: к примеру, две 
восьмерки выигрывают две пятерки (см. пример 1 ниже). 
Если же достоинства карт у игроков одинаковы, к примеру, 
у обоих игроков пара дам, то сравнивают карту наивысшего 
достоинства (см. пример 4 ниже); если же и эти карты одинаковы, 
сравнивают следующие две и т.д.

Допустим, два игрока сыграли 5 ставок следующим образом:

Ставка      1-й игрок       2-й игрок       Победитель
1       5♥ 5♣ 6♠ 7♠ K♦
Пара пятерок
    2♣ 3♠ 8♠ 8♦ T♦
Пара восьмерок
    2-й игрок
2       5♦ 8♣ 9♠ J♠ A♣
Старшая карта туз
    2♣ 5♣ 7♦ 8♠ Q♥
Старшая карта дама
    1-й игрок
3       2♦ 9♣ A♠ A♥ A♣
Три туза
    3♦ 6♦ 7♦ T♦ Q♦
Флаш, бубны
    2-й игрок
4       4♦ 6♣ 9♥ Q♥ Q♣
Пара дам
Старшая карта девятка
    3♦ 6♦ 7♥ Q♦ Q♠
Пара дам
Старшая карта семерка
    1-й игрок
5       2♥ 2♦ 4♣ 4♦ 4♠
Фул-хаус
Три четверки
    3♣ 3♦ 3♠ 9♠ 9♦
Фул-хаус
Три тройки
    1-й игрок
Файл poker.txt содержит одну тысячу различных ставок для игры двух игроков. 
В каждой строке файла приведены десять карт (отделенные одним пробелом): 
первые пять - карты 1-го игрока, оставшиеся пять - карты 2-го игрока. Можете считать, 
что все ставки верны (нет неверных символов или повторов карт), ставки каждого игрока не следуют 
в определенном порядке, и что при каждой ставке есть безусловный победитель.

Сколько ставок выиграл 1-й игрок?

Примечание: карты в текстовом файле обозначены в соответствии с английскими наименованиями достоинств и мастей: T - десятка, J - валет, Q - дама, K - король, A - туз; S - пики, C - трефы, H - червы, D - бубны.

'''
from time import time

def dosts():
    return {"2": 1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":9,"J":10,"Q":11,"K":12,"A":13} 

def masts():
    return {"S": 1,"C":2,"H":3,"D":4}

def open_file():
    with open("poker.txt", "r") as f:
        arr =[]
        for i in f:
            arr2=[]
            arr2.append(i[:14].split(" "))
            arr2.append(i[15:29].split(" "))
            arr.append(arr2)
        return arr

def check(res):
    if res[0][0] == True and res[1][0] == True:
        return chenge(res[0],res[1])
    elif res[0][0] == True and res[1][0] == False:
        return True
    elif res[0][0] == False and res[1][0] == True:
        return False    
    else:
        return 

def chenge(x,y): # Проверка выйграша
    if x[1]>y[1]:
        return True
    elif x[1]==y[1]:
        if type(x[2]) != list:
            if x[2]>y[2]:
                return True
            else:
                return False
        else:
            for i in range(len(x[2])-1,-1,-1):
                if x[2][i]>y[2][i]:
                    return True
                elif x[2][i]==y[2][i]:
                    break
                else:
                    return False
    else:
        return False

def royal_flash_1(ls): # 1. Роял-флаш: Десятка, валет, дама, король и туз одной масти.
    res = []
    for x in ls:
        mast = masts()
        str_ = []
        set_ = set()
        for i in x:
            str_.append(i[0])
            set_.add(i[1])
        str_.sort()
        if ("".join(str_)) == "AJKQT" and len(set_) == 1:
            res.append([True,mast[i[1]],None])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return straet_flash_2(ls)            

def straet_flash_2(ls): # 2 Стрейт-флаш: Любые пять карт одной масти по порядку.
    res = []
    for x in ls:
        dost = dosts()
        mast = masts()
        str_ = []
        set_ = set()
        for i in x:
            str_.append(dost[i[0]])
            set_.add(i[1])
        if len(set_) == 1:
            str_.sort()
            prover = [f for f in range(str_[0],str_[0]+5)]
            if str_ == prover:
                res.append([True,mast[i[1]], str_[-1]])
            else:
                res.append([False,None,None])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return kare_3(ls)

def kare_3(ls): # 3 Каре: Четыре карты одного достоинства.
    res = []
    for x in ls:
        str_ = []
        set_ = set()
        for i in x:
            str_.append(i[0])
        set_ = list(set(str_))
        if len(set_) == 2:
            if set_.count(set_[0]) == 4:
                res.append([True,set_[0],None])
            res.append([True,set_[1],None])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return full_hause_4(ls)

def full_hause_4(ls): # 4 Фул-хаус: Три карты одного достоинства и одна пара карт.
    res = []
    for x in ls:
        dost = dosts()
        str_ = []
        set_ = set()
        for i in x:
            str_.append(dost[i[0]])
            set_.add(dost[i[0]])
        set_ = list(set_)
        if len(set_) == 2:
            if str_.count(set_[0]) == 3 and str_.count(set_[1]) == 2:
                res.append([True,set_[0],None])
            elif str_.count(set_[0]) == 2 and str_.count(set_[1]) == 3:
                res.append([True,set_[1],None])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return flash_5(ls)

def flash_5(ls): # 5 Флаш: Все пять карт одной масти.
    res = []
    for x in ls:    
        mast = masts()
        str_ = []
        set_ = set()
        for i in x:
            set_.add(i[1])
        if len(set_) == 1:
            res.append([True,mast[i[1]],None])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return straet_6(ls)

def straet_6(ls): # 6  Стрейт: Все пять карт по порядку, любые масти.
    res = []
    for x in ls:
        dost = dosts()
        mast = masts()
        str_ =[]
        dic = {}
        for i in x:
            dic[dost[i[0]]]=i[1]
            str_.append(dost[i[0]])
        str_.sort()
        prover = [f for f in range(str_[0],str_[0]+5)]
        if str_ == prover:
            res.append([True,str_[-1],mast[dic[str_[-1]]]])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return three_7(ls)

def three_7(ls): # 7 Тройка: Три карты одного достоинства.
    res = []
    for x in ls:    
        dost = dosts()
        str_ =[]
        for i in x:
            str_.append(dost[i[0]])
        set_=list(set(str_))
        k=0
        for j in range(len(set_)):
            if str_.count(str_[j]) == 3:
                k = str_[j]
        if k != 0:
            res.append([True,k,None])
        else:
            res.append([False,None,None])
        
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return duble_8(ls)

def duble_8(ls): # 8 Две пары: Две различные пары карт
    res = []
    for x in ls:    
        dost = dosts()
        mast = masts()
        str_1 =[]
        str_2 =[]
        for i in x:
            str_1.append(dost[i[0]])
            str_2.append(mast[i[1]])
        set_ = list(set(str_1))
        if len(set_) == 3:
            max_1 = 0
            for j in str_1:
                if str_1.count(j)==2 and j > max_1:
                    max_1 = j
            max_2 = 0
            for ind,val in enumerate(str_1):
                if val == max_1 and str_2[ind] > max_2:
                    max_2 = str_2[ind]
            res.append([True,max_1,max_2])
        else:
            res.append([False,None,None])
    if check(res):
        return True
    elif check(res) == False:
        return False
    else:
        return pair_9(ls)

def pair_9(ls): # 9 Одна пара: Две карты одного достоинства
    res = []
    for x in ls:    
        dost = dosts()
        mast = masts()
        str_1 =[]
        str_2 =[]
        for i in x:
            str_1.append(dost[i[0]])
            str_2.append(mast[i[1]])
        set_ = list(set(str_1))
        if len(set_) == 4:
            for j in str_1:
                if str_1.count(j)==2:
                    max_1 = j
            new_str_1 = list(set(str_1))        
            new_str_1.remove(max_1)
            new_str_1.sort()
            res.append([True,max_1,new_str_1])
        else:
            res.append([False,None,None])
    z = check(res)
    if z == True:
        return True
    elif z == False:
        return False
    else:
        return adult_10(ls)

def adult_10(ls): # 10 Старшая карта: Карта наибольшего достоинства
    res = []
    for x in ls:    
        dost = dosts()
        mast = masts()
        str_ =[]
        dic = {}
        for i in x:
            str_.append(dost[i[0]])
            dic[dost[i[0]]]=mast[i[1]]
        res.append([True,max(str_),dic[max(str_)]])
    return chenge(res[0],res[1])

def main():
    start = time()
    player_1 = 0
    player =open_file()
    k = 0
    for i in player:
        k+=1
        while True:
            if royal_flash_1(i):
                player_1 += 1
                break
            else:
                break
            
    print(f"Ansver: {player_1} -ставок выиграл 1-й игрок")


    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
