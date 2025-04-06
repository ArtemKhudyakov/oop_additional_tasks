

def test_user_init(first_user, second_user):
    assert first_user.first_name == 'User'
    assert first_user.last_name == 'Userov'
    assert first_user.email == 'User@mail.com'
    assert first_user.username == 'User'
    assert len(first_user.task_in_list) == 2

    assert first_user.user_count == 2
    assert second_user.user_count == 2

    assert first_user.all_task_count == 5

    assert second_user.all_task_count == 5


def test_user_task_list_property(first_user):
    assert first_user.task_list ==('Купить огурцы, статус выполнения Ожидает старта, дата создания:  06.04.2025\n'
                                   'Купить помидоры, статус выполнения Ожидает старта, дата создания:  06.04.2025\n')

def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3
