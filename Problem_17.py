'''
Задача 17
Счет букв в числительных
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется 
всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?


Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) 
состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. 
Использование "and" при записи чисел соответствует правилам британского английского.
'''

num = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty',40:'forty',50:'fifty',60:'sixty',
70:'sevwnty',80:'eighty',90:'ninety',100:'hundred',1000:'one thousand'}

def list_number(num, number):
	return num[number]

def list_number_2(num, number):
	res_1 = (int(number/10))*10
	res_2 = number - res_1
	first = list_number(num, res_1)
	second = list_number(num, res_2)
	return(f"{first}-{second}")
	
def list_number_3(num, number):
	res_1 = (int(number/100))*100
	res_2 = number - res_1
	if res_2 in num:
		first = list_number(num, res_1/100)
		second = list_number(num,100)
		third = "and"
		fourth = list_number(num, res_2)
		return(f"{first} {second} {third} {fourth}")
	elif number%100 == 0:
		first = list_number(num, res_1/100)
		second = list_number(num,100)
		return(f"{first} {second}")
	else:
		first = list_number(num, res_1/100)
		second = list_number(num,100)
		third = "and"
		fourth = list_number_2(num, res_2)
		return(f"{first} {second} {third} {fourth}")

def cost(s):
	f= s.replace(" ","")
	f_1= f.replace("-","")
	return len(f_1)

n = 1000
result = 0
for number in range(1,n+1):
	if number in list(num.keys()) and number != 100:
		meaning = list_number(num, number)
		print(number, meaning)
		result += cost(meaning)
	elif 20<number<100:
		meaning = list_number_2(num, number)
		print(number, meaning)
		result += cost(meaning)
	elif 100<=number<1000:
		meaning = list_number_3(num, number)
		print(number, meaning)
		result += cost(meaning)
print(f"Понадобится для записи всех чисел от 1 до 1000 '{result}' букв.")


#########################################################################
# second option

nums = {
1:'one',
2:'two', 
3:'three', 
4:'four', 
5:'five', 
6:'six', 
7:'seven', 
8:'eight', 
9:'nine',
10:'ten', 
11:'eleven', 
12:'twelve', 
13:'thirteen', 
14:'fourteen', 
15:'fifteen', 
16:'sixteen',
17:'seventeen', 
18:'eighteen', 
19:'nineteen', 
20:'twenty', 
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'sevwnty',
80:'eighty',
90:'ninety'
}


def gen(n,dic):
	t =str(n)
	if dic.get(n,False):
		return dic[n]
	elif n<100:
		tr = n- int(t[1])
		return dic[tr] + dic[int(t[1])]
	elif n<1000:
		if t[1:3] == '00':
			return dic[int(t[0])] + 'hundret'
		else:
			return dic[int(t[0])] + 'hundretand'+ gen(int(t[1:3]), nums)
	elif n == 1000:
		return 'onethousand'

s = 0 
for i in range(1,1001):
	s+=len(gen(i,nums))
	print(gen(i,nums))
print(s)
	
