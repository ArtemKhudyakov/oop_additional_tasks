import pytest
from alternative_task.src.task import Task
from alternative_task.src.user import User


@pytest.fixture
def first_user():
    return User('User', 'User@mail.com', 'User', 'Userov',
                     [
                         Task("Купить огурцы", 'Купить огурцы для салата'),
                         Task("Купить помидоры", 'Купить помидоры для салата')
                     ]
                     )
@pytest.fixture
def second_user():
    return User('John', 'John@mail.com', 'John', 'Doe',
                     [
                         Task("Купить огурцы", 'Купить огурцы для салата'),
                         Task("Купить помидоры", 'Купить помидоры для салата'),
                         Task("Купить лук", 'Купить лук для салата')
                     ]
                     )


@pytest.fixture
def task():
    return Task("Купить огурцы", 'Купить огурцы для салата', created_at='20.04.2024')