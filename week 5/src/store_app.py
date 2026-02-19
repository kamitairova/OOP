from __future__ import annotations

from typing import List

from .cart import Cart
from .device import Device, Smartphone, Laptop, Tablet


def create_devices() -> List[Device]:
    """
    Create at least 20 devices with varying names, prices, and stock.
    """
    devices: List[Device] = [
        Smartphone("iPhone 13", 799, 10, 24, screen_size=6.1, battery_life=20),
        Smartphone("Samsung Galaxy S22", 749, 8, 24, screen_size=6.2, battery_life=22),
        Smartphone("Google Pixel 7", 599, 12, 24, screen_size=6.3, battery_life=24),
        Smartphone("Xiaomi 13", 699, 9, 18, screen_size=6.36, battery_life=23),
        Smartphone("OnePlus 11", 729, 7, 24, screen_size=6.7, battery_life=25),
        Smartphone("Nothing Phone (2)", 649, 6, 24, screen_size=6.7, battery_life=26),
        Smartphone("Sony Xperia 5", 799, 4, 24, screen_size=6.1, battery_life=18),

        Laptop("MacBook Pro 14", 1999, 5, 12, ram_size=16, processor_speed=3.2),
        Laptop("Dell XPS 13", 1299, 6, 24, ram_size=16, processor_speed=3.1),
        Laptop("Lenovo ThinkPad X1", 1499, 4, 36, ram_size=32, processor_speed=3.3),
        Laptop("HP Spectre x360", 1399, 7, 24, ram_size=16, processor_speed=3.0),
        Laptop("Asus ROG Zephyrus", 1799, 3, 24, ram_size=32, processor_speed=3.6),
        Laptop("Acer Swift 3", 799, 10, 12, ram_size=8, processor_speed=2.8),
        Laptop("Microsoft Surface Laptop", 1199, 5, 24, ram_size=16, processor_speed=3.0),

        Tablet("iPad Air", 599, 11, 12, screen_resolution="2360x1640", weight=461),
        Tablet("iPad Pro 11", 799, 6, 12, screen_resolution="2388x1668", weight=466),
        Tablet("Samsung Galaxy Tab S8", 699, 8, 24, screen_resolution="2560x1600", weight=507),
        Tablet("Xiaomi Pad 6", 399, 10, 18, screen_resolution="2880x1800", weight=490),
        Tablet("Amazon Fire HD 10", 149, 15, 12, screen_resolution="1920x1200", weight=465),
        Tablet("Lenovo Tab P11", 249, 9, 12, screen_resolution="2000x1200", weight=490),
    ]

    # Example: apply a discount to a few devices (optional demo)
    devices[0].apply_discount(5)   # iPhone 13 -5%
    devices[7].apply_discount(10)  # MacBook Pro -10%

    return devices


def show_devices(devices: List[Device]) -> None:
    print("\n--- Available Devices ---")
    for idx, d in enumerate(devices, start=1):
        print(f"{idx}. {d}")  # __str__ includes type + details


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    devices = create_devices()
    cart = Cart()

    while True:
        print("\n=== Electronic Device Store ===")
        print("1. Show Devices (add to cart)")
        print("2. Show Cart (and checkout)")
        print("3. Exit")

        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            show_devices(devices)

            pick = input("\nEnter device number to add (or press Enter to go back): ").strip()
            if not pick:
                continue

            try:
                idx = int(pick)
            except ValueError:
                print("Invalid selection.")
                continue

            if idx < 1 or idx > len(devices):
                print("Invalid device number.")
                continue

            amount = read_int("Enter quantity: ")
            device = devices[idx - 1]

            if cart.add_device(device, amount):
                print("Added to cart.")
            else:
                print("Not enough stock or invalid quantity.")

        elif choice == "2":
            cart.print_items()
            if cart.items:
                do_checkout = input("Checkout now? (y/n): ").strip().lower()
                if do_checkout == "y":
                    cart.checkout()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1-3.")


if __name__ == "__main__":
    main()
