from datetime import datetime
from user import User


def test_user_age_is_int():
    u = User(1, "A", "B", datetime(2000, 1, 1))
    assert isinstance(u.get_age(), int)


def test_get_details_contains_id():
    u = User(10, "John", "Doe", datetime(2000, 1, 1))
    details = u.get_details()
    assert "User ID: 10" in details
