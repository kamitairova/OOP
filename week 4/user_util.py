from __future__ import annotations
import random
import re
import string
from datetime import datetime


class UserUtil:
    """
    Utility class with static methods:
      - generate_user_id
      - generate_password
      - is_strong_password
      - generate_email
      - validate_email
    """

    @staticmethod
    def generate_user_id() -> int:
        """
        Generates unique new user_id with 9 digits.
        First two digits = current year last 2 digits.
        Remaining 7 digits are random.
        Example for 2026: 26XXXXXXX
        """
        year_two = str(datetime.now().year)[-2:]  # e.g., "26"
        random_part = "".join(str(random.randint(0, 9)) for _ in range(7))
        return int(year_two + random_part)

    @staticmethod
    def generate_password(length: int = 10) -> str:
        """
        Generates new password:
          - minimum 8 characters
          - at least 1 uppercase, 1 lowercase, 1 digit, 1 special character
        """
        if length < 8:
            length = 8

        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special_chars = "!@#$%^&*()-_=+[]{};:,.?/\\|"
        special = random.choice(special_chars)

        remaining_len = length - 4
        all_chars = string.ascii_letters + string.digits + special_chars
        remaining = [random.choice(all_chars) for _ in range(remaining_len)]

        password_list = [upper, lower, digit, special] + remaining
        random.shuffle(password_list)
        return "".join(password_list)

    @staticmethod
    def is_strong_password(password: str) -> bool:
        """
        Checks if password:
          - len >= 8
          - has uppercase + lowercase
          - has digit
          - has special
        """
        if password is None or len(password) < 8:
            return False

        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)

        return has_upper and has_lower and has_digit and has_special

    @staticmethod
    def generate_email(name: str, surname: str, domain: str) -> str:
        """
        Generates email: name.surname@domain
        Example: john.doe@domain.com
        """
        name = str(name).strip().lower()
        surname = str(surname).strip().lower()
        domain = str(domain).strip().lower()
        return f"{name}.{surname}@{domain}"

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates email format: name.surname@domain.tld
        Example: john.doe@gmail.com
        """
        if email is None:
            return False

        pattern = r"^[a-z]+(\.[a-z]+)+@[a-z0-9-]+(\.[a-z0-9-]+)+$"
        return re.match(pattern, email.strip().lower()) is not None
