"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""

import time

class Timer:

    # def __init__(self):
    #     self.start = time.time()

    def __enter__(self):
        self.start = time.time()
        return self



    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed_time = self.end - self.start
        print("Execution time:", self.elapsed_time)
        return self.elapsed_time


with Timer() as timer:
    # блок кода
    time.sleep(1)
    # код для проверки 
    print("Execution time:", timer.elapsed_time)
