import datetime


class Task:
    name:str
    description:str
    status:str
    created_at: str

    def __init__(self, name:str, description:str, status:str = "Ожидает старта", created_at:str = None):
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")

if __name__ == '__main__':
    task = Task("Купить огурцы", 'Купить огурцы для салата')
    print(task.name)
    print(task.description)
    print(task.created_at)
    print(task.status)