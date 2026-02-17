from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil


def main():
    UserService.users.clear()

    print("=== USER MANAGEMENT DEMO ===\n")

    user_id = UserUtil.generate_user_id()
    user = User(user_id, "Kamilla", "Tairova", datetime(2004, 8, 10))

    user.password = UserUtil.generate_password()
    user.email = UserUtil.generate_email(user.name, user.surname, "gmail.com")

    print("Created user:")
    print(user.get_details())
    print("Password strong:", UserUtil.is_strong_password(user.password))
    print("Email valid:", UserUtil.validate_email(user.email))
    print()

    added = UserService.add_user(user)
    print("Added to UserService:", added)
    print("Number of users:", UserService.get_number())
    print()

    found = UserService.find_user(user_id)
    print("Found user:")
    print(found.get_details() if found else "Not found")
    print()

    update_obj = User(user_id, "Kamilla", "UpdatedSurname", datetime(2004, 8, 10))
    update_obj.email = UserUtil.generate_email(update_obj.name, update_obj.surname, "outlook.com")

    updated = UserService.update_user(user_id, update_obj)
    print("Updated:", updated)
    print("After update:")
    print(UserService.find_user(user_id))
    print()

    deleted = UserService.delete_user(user_id)
    print("Deleted:", deleted)
    print("Number of users:", UserService.get_number())


if __name__ == "__main__":
    main()
