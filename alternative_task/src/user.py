from alternative_task.src.task import Task


class User:
    username:str
    email:str
    first_name:str
    last_name:str
    task_list:list
    user_count:int = 0
    all_task_count:int = 0


    def __init__(self, username:str, email:str, first_name:str, last_name:str, task_list:list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.user_count += 1
        User.all_task_count += len(task_list) if task_list else 0


    @property
    def task_list(self):
        task_str = ''
        for task in self.__task_list:
            task_str += f'{task.name}, статус выполнения {task.status}, дата создания:  {task.created_at}\n'
        return task_str

    @task_list.setter
    def task_list(self, task:Task):
        self.__task_list.append(task)
        User.all_task_count += 1

    @property
    def task_in_list(self):
        return self.__task_list


if __name__ == '__main__':
    task1 = Task("Купить огурцы", 'Купить огурцы для салата')
    task2 = Task("Купить помидоры", 'Купить помидоры для салата')
    task3 = Task("Купить лук", 'Купить лук для салата')
    task4 = Task("Купить перец", 'Купить перец для салата')

    user=User('User', 'User@mail.com', 'User', 'Userov', [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.user_count)
    print(user.all_task_count)

    task5 = Task("Купить картошку", 'Купить картошку для супа')
    user.task_list = task5

    print(user.task_list)
    print(user.all_task_count)