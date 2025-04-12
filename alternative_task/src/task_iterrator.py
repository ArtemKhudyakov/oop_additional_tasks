from alternative_task.src.task import Task
from alternative_task.src.user import User

class TaskIterator:
    def __init__(self, user_obj):
        self.user = user_obj
        self.index = 0



    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.user.task_in_list):
            task = self.user.task_in_list[self.index]
            self.index += 1
            return task
        else:
            raise StopIteration


if __name__ == '__main__':
    task1 = Task("Купить огурцы", 'Купить огурцы для салата')
    task2 = Task("Купить помидоры", 'Купить помидоры для салата')
    task3 = Task("Купить лук", 'Купить лук для салата')
    task4 = Task("Купить перец", 'Купить перец для салата')

    user = User('User', 'User@mail.com', 'User', 'Userov', [task1, task2, task3, task4])

    art_task1 = Task("Альтернативную задача", "Совместно с наставником прорешать альтернативную задачу")
    art_task2 = Task("Домашняя работа", "Выполнить домашнюю работу")

    user2 = User("Tema", "tema@mail.com", "Artem", "Khudyakov", [art_task1, art_task2])

    iterator = TaskIterator(user)
    iterator2 = TaskIterator(user2)


    print('\nuser1\n')
    for task in iterator:
        print(task)

    print('\nПовтор\n')
    for task in iterator:
        print(task)


    print('\nuser2\n')
    for task in iterator2:
        print(task)

    print('\nПовтор\n')
    for task in iterator2:
        print(task)