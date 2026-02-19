from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from .device import Device


@dataclass
class Cart:
    """
    Shopping cart storing (device, amount) pairs.

    Attributes:
        items: list of tuples (Device, amount)
        total_price: total price of items in cart
    """
    items: List[Tuple[Device, int]] = field(default_factory=list)
    total_price: float = 0.0

    def _recalculate_total(self) -> None:
        self.total_price = sum(device.price * amount for device, amount in self.items)

    def add_device(self, device: Device, amount: int) -> bool:
        """
        Adds a specified quantity of a device to the cart if it’s available.
        Updates total_price.

        Returns True if added, False if not enough stock or invalid amount.
        """
        amount = int(amount)
        if amount <= 0:
            return False
        if not device.is_available(amount):
            return False

        # If device already in cart, increase amount
        for i, (d, a) in enumerate(self.items):
            if d is device:
                self.items[i] = (d, a + amount)
                self._recalculate_total()
                return True

        self.items.append((device, amount))
        self._recalculate_total()
        return True

    def remove_device(self, device: Device, amount: int) -> bool:
        """
        Removes a specified quantity of a device from the cart.
        If amount >= existing amount, removes the item completely.

        Returns True if something was removed, False otherwise.
        """
        amount = int(amount)
        if amount <= 0:
            return False

        for i, (d, a) in enumerate(self.items):
            if d is device:
                if amount >= a:
                    self.items.pop(i)
                else:
                    self.items[i] = (d, a - amount)
                self._recalculate_total()
                return True
        return False

    def get_total_price(self) -> float:
        return self.total_price

    def print_items(self) -> None:
        if not self.items:
            print("Cart is empty.")
            return

        print("--- Cart Items ---")
        for idx, (device, amount) in enumerate(self.items, start=1):
            line_total = device.price * amount
            print(f"{idx}. {device.name} | qty={amount} | unit={device.price:.2f} | line={line_total:.2f}")
        print(f"TOTAL: {self.total_price:.2f}")

    def checkout(self) -> bool:
        """
        Ensures all devices are available in the specified quantity.
        If they are, reduce stock and print a receipt.

        Returns True if checkout succeeded, False otherwise.
        """
        if not self.items:
            print("Cart is empty. Nothing to checkout.")
            return False

        # Validate availability
        for device, amount in self.items:
            if not device.is_available(amount):
                print(f"Checkout failed: '{device.name}' has insufficient stock.")
                return False

        # Reduce stock and print receipt
        print("=== RECEIPT ===")
        total = 0.0
        for device, amount in self.items:
            device.reduce_stock(amount)
            line_total = device.price * amount
            total += line_total
            print(f"{device.name} x{amount} @ {device.price:.2f} = {line_total:.2f}")

        print(f"TOTAL: {total:.2f}")
        print("Thank you for your purchase!")

        # Clear cart
        self.items.clear()
        self._recalculate_total()
        return True
