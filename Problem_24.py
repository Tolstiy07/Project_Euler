'''
Задача 24
Словарные перестановки
Перестановка - это упорядоченная выборка объектов. К примеру, 
3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4.
 Если все перестановки приведены в порядке возрастания или алфавитном порядке, 
 то такой порядок будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 
 представлены ниже:

012   021   102   120   201   210




Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
'''
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cont = 0
for i in range(len(num)):
	num2 = num.copy()
	res_1 =str(num[i])
	num2.remove(num[i])
	for i in range(len(num2)):
		num3 = num2.copy()
		res_2 =str(num2[i])
		num3.remove(num2[i])
		for i in range(len(num3)):
			num4 = num3.copy()
			res_3 =str(num3[i])
			num4.remove(num3[i])
			for i in range(len(num4)):
				num5 = num4.copy()
				res_4 =str(num4[i])
				num5.remove(num4[i])
				for i in range(len(num5)):
					num6 = num5.copy()
					res_5 =str(num5[i])
					num6.remove(num5[i])
					for i in range(len(num6)):
						num7 = num6.copy()
						res_6 =str(num6[i])
						num7.remove(num6[i])
						for i in range(len(num7)):
							num8 = num7.copy()
							res_7 =str(num7[i])
							num8.remove(num7[i])
							for i in range(len(num8)):
								num9 = num8.copy()
								res_8 =str(num8[i])
								num9.remove(num8[i])
								for i in range(len(num9)):
									num0 = num9.copy()
									res_9 =str(num9[i])
									num0.remove(num9[i])

									cont +=1
									if cont == 1000000:
										print("Mиллионная словарная перестановка из ")
										print(f"цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9 - {res_1 + res_2 + res_3 + res_4 + res_5 + res_6 + res_7 + res_8 + res_9 + str(num0[0])}")
										exit()