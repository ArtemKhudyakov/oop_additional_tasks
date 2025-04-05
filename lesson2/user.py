"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    name: str
    password: str

    is_admin: bool = False
    _is_admin: bool = False
    _is_logged_in: bool


    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self._is_admin = False
        self._is_logged_in = False

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_admin(self):
        return self._is_admin

    def login(self, password):
        if password == self.__password:
            print(True)
            self._is_logged_in = True
        else:
            print(False)
            self._is_logged_in = False

    @property
    def is_logged_in(self):
        if self._is_logged_in:
            return True
        else:
            return False

    def logout(self):
        self._is_logged_in = False








# код для проверки 
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False
#
user1.password = "newpassword"
print(user1.password)  # newpassword
#
user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
print(user1.is_logged_in)

user1.logout()

print(user1.is_logged_in)
