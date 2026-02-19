import pytest
from src.device import Device, Smartphone, Laptop, Tablet


def test_device_discount():
    d = Device("Test", 100, 5, 12)
    d.apply_discount(10)
    assert d.price == pytest.approx(90.0)


def test_device_availability_and_reduce_stock():
    d = Device("Test", 100, 5, 12)
    assert d.is_available(3) is True
    d.reduce_stock(3)
    assert d.stock == 2
    assert d.is_available(3) is False


def test_smartphone_str_contains_type():
    s = Smartphone("Phone", 500, 2, 12, screen_size=6.1, battery_life=20)
    assert "Smartphone" in str(s)


def test_laptop_str_contains_type():
    l = Laptop("Laptop", 1000, 1, 24, ram_size=16, processor_speed=3.2)
    assert "Laptop" in str(l)


def test_tablet_str_contains_type():
    t = Tablet("Tablet", 300, 4, 12, screen_resolution="2000x1200", weight=500)
    assert "Tablet" in str(t)
