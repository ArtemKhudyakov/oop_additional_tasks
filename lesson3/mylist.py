"""
Напишите класс MyList, представляющий собой список, имеющий следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __repr__(self): магический метод, возвращающий строковое представление списка,
которое можно использовать для создания нового объекта класса MyList;
- __str__(self): магический метод, возвращающий строковое представление списка;
- __len__(self): магический метод, возвращающий длину списка;
- __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
"""


class MyList:
    def __init__(self, data:list=None):
        self.data = data

    def __repr__(self):
        return f"MyList({self.data})"

    def __str__(self):
        return f"({self.data})"

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        new_list = MyList(self.data)
        new_list.data.extend(other.data)

        return new_list

# код для проверки 
my_list1 = MyList([1, 2, 3])
print(repr(my_list1))  # MyList([1, 2, 3])
print(str(my_list1))  # [1, 2, 3]
print(len(my_list1))  # 3

my_list2 = MyList([4, 5, 6])
my_list3 = MyList([7, 8, 9])
my_list4 = my_list1 + my_list2 + my_list3
print(my_list4)  # [1, 2, 3, 4, 5, 6]

