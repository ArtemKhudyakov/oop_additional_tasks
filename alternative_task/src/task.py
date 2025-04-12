import datetime


class Task:
    name:str
    description:str
    status:str
    created_at: str
    run_time: int

    def __init__(self, name:str, description:str, status:str = "Ожидает старта", created_at:str = None, run_time:int = 0):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")
        self.run_time = run_time


    def __str__(self):
        return f"{self.name}, статус выполнения: {self.status}, дата создания: {self.created_at}, время на выполнеие задачи: {self.run_time}"


    def __add__(self, other):
        return self.run_time + other.run_time

    @classmethod
    def new_task(cls, name, description:str, status:str = "Ожидает старта", created_at:str = None, run_time:int = 0):
        return cls(name, description, status, created_at, run_time)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date:str):
        if datetime.datetime.strptime(new_date, "%d.%m.%Y").date() < datetime.datetime.now().date():
            print ("Нельзя изменить дату создания на дату из прошлого")
            return
        else:
            self.__created_at = new_date



if __name__ == '__main__':
    task = Task("Купить огурцы", 'Купить огурцы для салата', run_time=60)
    print(task.name)
    print(task.description)
    print(task.created_at)
    print(task.status)

    task2 = Task.new_task("Купить билеты", "купить билеты на самолет", run_time = 180)
    print(task2)
    print(task2.name)
    print(task2.description)
    print(task2.created_at)
    print(task2.status)

    task2.created_at = '13.04.2025'
    print(task2.created_at)


    print (task + task2)