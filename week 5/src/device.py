from __future__ import annotations

from dataclasses import dataclass
from typing import Union


Number = Union[int, float]


@dataclass
class Device:
    """
    Base class for all electronic devices.

    Attributes:
        name (str): Device name.
        price (float): Current device price.
        stock (int): Units available in store.
        warranty_period (int): Warranty in months.
    """
    name: str
    price: float
    stock: int
    warranty_period: int

    def __post_init__(self) -> None:
        self.name = str(self.name).strip()
        self.price = float(self.price)
        self.stock = int(self.stock)
        self.warranty_period = int(self.warranty_period)

        if not self.name:
            raise ValueError("Device name cannot be empty")
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative")
        if self.warranty_period < 0:
            raise ValueError("Warranty period cannot be negative")

    def display_info(self) -> str:
        """Displays the basic details of the device."""
        return (
            f"Name: {self.name} | Price: {self.price:.2f} | "
            f"Stock: {self.stock} | Warranty: {self.warranty_period} months"
        )

    def __str__(self) -> str:
        return self.display_info()

    def apply_discount(self, discount_percentage: Number) -> None:
        """
        Reduces the price by a specified discount percentage.

        Args:
            discount_percentage: Percentage in range [0, 100].
        """
        discount_percentage = float(discount_percentage)
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("discount_percentage must be between 0 and 100")
        self.price *= (1 - discount_percentage / 100)

    def is_available(self, amount: int) -> bool:
        """Checks if the device is available in the required quantity."""
        amount = int(amount)
        if amount <= 0:
            return False
        return self.stock >= amount

    def reduce_stock(self, amount: int) -> None:
        """Reduces the stock by the specified quantity when a purchase is made."""
        amount = int(amount)
        if amount <= 0:
            raise ValueError("amount must be > 0")
        if amount > self.stock:
            raise ValueError("Insufficient stock to reduce")
        self.stock -= amount


@dataclass
class Smartphone(Device):
    """
    Smartphone device.
    Additional attributes:
        screen_size (float): Inches.
        battery_life (int): Hours.
    """
    screen_size: float = 0.0
    battery_life: int = 0

    def __post_init__(self) -> None:
        super().__post_init__()
        self.screen_size = float(self.screen_size)
        self.battery_life = int(self.battery_life)
        if self.screen_size <= 0:
            raise ValueError("screen_size must be > 0")
        if self.battery_life <= 0:
            raise ValueError("battery_life must be > 0")

    def display_info(self) -> str:
        return (
            f"[Smartphone] {super().display_info()} | "
            f"Screen: {self.screen_size:.1f}\" | Battery: {self.battery_life}h"
        )

    def __str__(self) -> str:
        return self.display_info()

    def make_call(self) -> str:
        return f"{self.name}: Making a call..."

    def install_app(self) -> str:
        return f"{self.name}: Installing an app..."


@dataclass
class Laptop(Device):
    """
    Laptop device.
    Additional attributes:
        ram_size (int): GB.
        processor_speed (float): GHz.
    """
    ram_size: int = 0
    processor_speed: float = 0.0

    def __post_init__(self) -> None:
        super().__post_init__()
        self.ram_size = int(self.ram_size)
        self.processor_speed = float(self.processor_speed)
        if self.ram_size <= 0:
            raise ValueError("ram_size must be > 0")
        if self.processor_speed <= 0:
            raise ValueError("processor_speed must be > 0")

    def display_info(self) -> str:
        return (
            f"[Laptop] {super().display_info()} | "
            f"RAM: {self.ram_size}GB | CPU: {self.processor_speed:.2f}GHz"
        )

    def __str__(self) -> str:
        return self.display_info()

    def run_program(self) -> str:
        return f"{self.name}: Running a program..."

    def use_keyboard(self) -> str:
        return f"{self.name}: Typing on the keyboard..."


@dataclass
class Tablet(Device):
    """
    Tablet device.
    Additional attributes:
        screen_resolution (str): e.g., '2048x1536'
        weight (int): grams
    """
    screen_resolution: str = ""
    weight: int = 0

    def __post_init__(self) -> None:
        super().__post_init__()
        self.screen_resolution = str(self.screen_resolution).strip()
        self.weight = int(self.weight)
        if not self.screen_resolution:
            raise ValueError("screen_resolution cannot be empty")
        if self.weight <= 0:
            raise ValueError("weight must be > 0")

    def display_info(self) -> str:
        return (
            f"[Tablet] {super().display_info()} | "
            f"Resolution: {self.screen_resolution} | Weight: {self.weight}g"
        )

    def __str__(self) -> str:
        return self.display_info()

    def browse_internet(self) -> str:
        return f"{self.name}: Browsing the internet..."

    def use_touchscreen(self) -> str:
        return f"{self.name}: Using touchscreen..."
