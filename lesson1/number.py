"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:
    value:int

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, addition):
        added = self.value+addition
        return added

    def substruct(self, subtraction):
        self.value -= subtraction


# код для проверки 
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substruct(5)
print(n.get())  # 5
