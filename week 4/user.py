from __future__ import annotations
from datetime import date, datetime


class User:
    """
    Represents a user record.

    Instance variables (as required):
      - user_id: int
      - name: str
      - surname: str
      - email: str
      - password: str
      - birthday: datetime
    """

    def __init__(self, user_id: int, name: str, surname: str, birthday: datetime):
        self.user_id = int(user_id)
        self.name = str(name)
        self.surname = str(surname)
        self.birthday = birthday

        self.email: str | None = None
        self.password: str | None = None

    def get_details(self) -> str:
        """
        Returns a formatted string containing user details.
        """
        email_str = self.email if self.email is not None else "N/A"
        age = self.get_age()
        bday_str = self.birthday.strftime("%Y-%m-%d")
        return (
            f"User ID: {self.user_id} | "
            f"Name: {self.name} {self.surname} | "
            f"Birthday: {bday_str} | "
            f"Age: {age} | "
            f"Email: {email_str}"
        )

    def get_age(self) -> int:
        """
        Computes and returns the user's age.
        """
        today = date.today()
        born = self.birthday.date() if isinstance(self.birthday, datetime) else self.birthday

        age = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            age -= 1
        return age

    def __str__(self) -> str:
        return self.get_details()
