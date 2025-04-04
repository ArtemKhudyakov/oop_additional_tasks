

def test_user_init(first_user, second_user):
    assert first_user.first_name == 'User'
    assert first_user.last_name == 'Userov'
    assert first_user.email == 'User@mail.com'
    assert first_user.username == 'User'
    assert len(first_user.task_list) == 2

    assert first_user.user_count == 2
    assert second_user.user_count == 2

    assert first_user.all_task_count == 5

    assert second_user.all_task_count == 5