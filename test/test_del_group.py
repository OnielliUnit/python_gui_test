import random

def test_delete_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("group 1")
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.delete_some_group(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)