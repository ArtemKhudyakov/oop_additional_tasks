from alternative_task.src.task import Task
import datetime

def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == '20.04.2024'

def test_task_create():
    task = Task("Купить билеты", "купить билеты на самолет")
    assert task.name == "Купить билеты"
    assert task.description == 'купить билеты на самолет'
    assert task.status == "Ожидает старта"
    assert task.created_at == datetime.datetime.now().strftime("%d.%m.%Y")

def test_task_update(capsys, task):
    task.created_at = "03.04.2025"
    message = capsys.readouterr()


    assert message.out.strip() == "Нельзя изменить дату создания на дату из прошлого"
    assert task.created_at == '20.04.2024'

    task.created_at = datetime.datetime.now().strftime("%d.%m.%Y")
    assert task.created_at == datetime.datetime.now().strftime("%d.%m.%Y")

    task.created_at = "03.04.2029"
    assert task.created_at == "03.04.2029"