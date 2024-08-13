'''
Задача 39
Целые прямоугольные треугольники
Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, 
то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?
'''
from time import time

def main():
	print("Размеры прямоугольных треугольников:")
	start = time()
	arr =[]
	max_ = 0
	for a in range(1,1000):
		for b in range(a+1,1000):
			c = (a**2 + b**2)**0.5
			if c%1 == 0 and (a+b+c)<=1000:
				arr.append(a+b+int(c))
				if (a+b+int(c)) == 840:
					print(a,b,int(c))
	arr2 = sorted(list(set(arr)))
	for x in arr2:
		if arr.count(x)>max_:
			max_ = arr.count(x)
			max_x = x
	print(f"периметр их {max_x} дает максимальное число решений {max_}")
	print(f"Program running time {round(time()-start,2)} sec.")
if __name__=="__main__":
	main()