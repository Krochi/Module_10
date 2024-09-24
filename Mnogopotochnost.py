# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
# Выполнение:
# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.
# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
# Создайте список названий файлов в соответствии с названиями файлов архива.
# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
# Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool.
# Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов.
# Измерьте время выполнения и выведите его в консоль.
# Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
# предварительно закомментировав другой.
#
# Пример результата выполнения программы:
# Выполняемый код:
# def read_info(name):
# ...
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
#
# # Линейный вызов
#
# # Многопроцессный
#
# Вывод на консоль, 2 запуска (результаты могут отличаться):
# 0:00:03.046163 (линейный)
# 0:00:01.092300 (многопроцессный)
#
# Примечания:
# Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
# Выводить или возвращать список all_data в функции не нужно. Можете сделать это, но кол-во информации в
# файлах достигает - 10^9 строк.

#import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            lines = file.readline()
            if not lines:
                break
            all_data.append(lines.split())

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    start_time = time.time()
    for file in filenames:
        read_info(file)
    end_time = time.time()
    print(f"Линейный вызов: {end_time - start_time}")


    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time}")




