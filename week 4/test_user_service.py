from datetime import datetime
from user import User
from user_service import UserService


def setup_function():
    UserService.users.clear()


def test_add_and_find_user():
    u = User(101, "John", "Doe", datetime(2000, 1, 1))
    assert UserService.add_user(u) is True
    assert UserService.find_user(101) is not None


def test_add_duplicate_user_fails():
    u1 = User(101, "John", "Doe", datetime(2000, 1, 1))
    u2 = User(101, "Jane", "Doe", datetime(2000, 1, 1))
    assert UserService.add_user(u1) is True
    assert UserService.add_user(u2) is False


def test_delete_user():
    u = User(101, "John", "Doe", datetime(2000, 1, 1))
    UserService.add_user(u)
    assert UserService.delete_user(101) is True
    assert UserService.find_user(101) is None


def test_update_user():
    u = User(101, "John", "Doe", datetime(2000, 1, 1))
    UserService.add_user(u)

    update_obj = User(101, "Johnny", "Doe", datetime(2000, 1, 1))
    update_obj.email = "johnny.doe@gmail.com"

    assert UserService.update_user(101, update_obj) is True
    updated = UserService.find_user(101)
    assert updated.name == "Johnny"
    assert updated.email == "johnny.doe@gmail.com"


def test_get_number():
    assert UserService.get_number() == 0
    UserService.add_user(User(1, "A", "B", datetime(2000, 1, 1)))
    UserService.add_user(User(2, "C", "D", datetime(2000, 1, 1)))
    assert UserService.get_number() == 2
