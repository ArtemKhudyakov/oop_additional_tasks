"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""
import pathlib as p
import os


class Logger:


    def __init__(self, filename='logs.txt'):

        lesson3_path = p.Path(__file__).parent
        logs_dir = lesson3_path / 'logs'
        os.makedirs(logs_dir, exist_ok=True)
        self.filename = logs_dir / filename



    def __call__(self, message):
        with open(self.filename, 'a', encoding='utf-8') as log_file:
            log_file.write(message + '\n')

    def __repr__(self):
        return f"Logger(filename='{self.filename}')"


# код для проверки
logger = Logger("log.txt")
logger("This is a test message.")
