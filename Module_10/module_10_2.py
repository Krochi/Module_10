import time
from time import sleep
from threading import Thread

total_enemies = 100

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0


    def run(self):
        global total_enemies
        print(f'{self.name}, проснитесь, на нас напали ')
        while total_enemies > 0:
            time.sleep(1)
            self.days += 1
            total_enemies -= self.power

            if total_enemies < 0:
                total_enemies = 0

            print(f"{self.name} сражается {self.days} день(дня)..., осатлось {total_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)


#Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились")

            