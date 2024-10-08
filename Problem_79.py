'''
Задача 79
Вычисление пароля
Для проведения операций с банковскими счетами онлайн распространен метод безопасности, заключающийся в том, что пользователя просят указать три случайные символа его кода доступа. К примеру, если код доступа пользователя 531278, у него могут попросить ввести 2-й, 3-й и 5-й символы, и ожидаемым ответом будет 317.

В текстовом файле keylog.txt содержится 50 удачных попыток авторизации.

Учитывая, что три символа кода всегда запрашивают по их порядку в коде, проанализируйте файл с целью определения наиболее короткого секретного кода доступа неизвестной длины.




'''
from time import time

def main():
    start = time()


    print(f"Program running time {round(time() - start, 2)} sec.")

if __name__ == "__main__":
    main()
