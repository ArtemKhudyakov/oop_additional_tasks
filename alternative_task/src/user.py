


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
        self.task_list = task_list if task_list else []
        User.user_count += 1
        User.all_task_count += len(task_list) if task_list else 0

if __name__ == '__main__':
