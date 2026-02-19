from src.device import Device
from src.cart import Cart


def test_add_device_updates_total():
    d = Device("Test", 50, 10, 12)
    c = Cart()
    assert c.add_device(d, 2) is True
    assert c.get_total_price() == 100.0


def test_add_device_not_enough_stock():
    d = Device("Test", 50, 1, 12)
    c = Cart()
    assert c.add_device(d, 2) is False
    assert c.get_total_price() == 0.0


def test_remove_device_reduces_total():
    d = Device("Test", 50, 10, 12)
    c = Cart()
    c.add_device(d, 3)  # total 150
    assert c.remove_device(d, 1) is True  # now 2 -> 100
    assert c.get_total_price() == 100.0


def test_checkout_reduces_stock_and_clears_cart(capsys):
    d = Device("Test", 50, 10, 12)
    c = Cart()
    c.add_device(d, 4)  # buy 4
    ok = c.checkout()
    captured = capsys.readouterr()
    assert ok is True
    assert "RECEIPT" in captured.out
    assert d.stock == 6
    assert len(c.items) == 0
