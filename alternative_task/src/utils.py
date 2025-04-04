import json
import os
import pathlib as p
from alternative_task.src.task import Task
from alternative_task.src.user import User


# Получаем имя модуля
# module_name = p.Path(__file__).stem
file_name = '30 09_30_4766a8b2c7152634.42242192data.json'
def read_json(file_name):
# Путь к корневой папке
    current_file_path = p.Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent.parent

    json_path = f"{project_root_path}/alternative_task/data/{file_name}"
    with open(json_path, "r", encoding='UTF-8') as f:
        data = json.load(f)
    return data

def create_objects(data):
    users = []
    for user in data:
        tasks = []
        for task in user['task_list']:
            tasks.append(Task(**task))
        user['task_list'] = tasks
        users.append(User(**user))
    return users


if __name__ == '__main__':
    json_data = read_json(file_name)
    users = create_objects(json_data)

    print (users)
    print (users[0].username)
    print (users[0].task_list[0].name)
