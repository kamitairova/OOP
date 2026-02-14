import pytest
from personal_account import PersonalAccount

def test_deposit_increases_balance():
    acc = PersonalAccount(1, "Test")
    acc.deposit(100)
    assert acc.get_balance() == 100

def test_withdraw_decreases_balance():
    acc = PersonalAccount(1, "Test")
    acc.deposit(100)
    acc.withdraw(40)
    assert acc.get_balance() == 60

def test_withdraw_more_than_balance_raises():
    acc = PersonalAccount(1, "Test")
    acc.deposit(50)
    with pytest.raises(ValueError):
        acc.withdraw(60)

def test_operator_add_works_like_deposit():
    acc = PersonalAccount(1, "Test")
    acc + 25
    assert acc.get_balance() == 25

def test_operator_sub_works_like_withdraw():
    acc = PersonalAccount(1, "Test")
    acc.deposit(30)
    acc - 10
    assert acc.get_balance() == 20