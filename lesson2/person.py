"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""

import datetime

class Person:
    name:str
    age:int

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print (f"{self.__name}, возраст {self.__age}")

    @property
    def name(self):
        return self.__name

    @classmethod
    def from_birth_year(cls, name, birth_year):

        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return Person(name, age)

    @classmethod
    def is_adult(cls, age):
        if age >= 18:
            return True
        else:
            return False




# код для проверки 
person1 = Person("John", 28)
person1.display()  # John is 28 years old

person2 = Person.from_birth_year("Mike", 1995)
person2.display()  # Mike is 26 years old

print(person2.name)

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
