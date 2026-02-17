from __future__ import annotations
from typing import Dict, Optional
from user import User


class UserService:
    """
    Manages users using class attribute 'users' (dictionary).
    Key: user_id, Value: User object
    """

    users: Dict[int, User] = {}

    @classmethod
    def add_user(cls, user: User) -> bool:
        """
        Adds a User object to users.
        Returns True if added, False if user_id already exists.
        """
        if user.user_id in cls.users:
            return False
        cls.users[user.user_id] = user
        return True

    @classmethod
    def find_user(cls, user_id: int) -> Optional[User]:
        """
        Searches for a user by user_id.
        Returns the User object if found, otherwise None.
        """
        return cls.users.get(int(user_id))

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        """
        Removes a user from users by user_id.
        Returns True if deleted, False if not found.
        """
        user_id = int(user_id)
        if user_id not in cls.users:
            return False
        del cls.users[user_id]
        return True

    @classmethod
    def update_user(cls, user_id: int, user_update: User) -> bool:
        """
        Updates user attributes using user_update object arguments.
        Only updates fields that are not None (or non-empty where relevant).
        Returns True if updated, False if user not found.
        """
        existing = cls.find_user(user_id)
        if existing is None:
            return False

        if getattr(user_update, "name", None):
            existing.name = user_update.name
        if getattr(user_update, "surname", None):
            existing.surname = user_update.surname
        if getattr(user_update, "birthday", None):
            existing.birthday = user_update.birthday

        if getattr(user_update, "email", None):
            existing.email = user_update.email
        if getattr(user_update, "password", None):
            existing.password = user_update.password

        return True

    @classmethod
    def get_number(cls) -> int:
        """
        Returns number of users currently stored.
        """
        return len(cls.users)
