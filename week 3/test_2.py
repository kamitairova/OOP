from personal_account import PersonalAccount


def main():
    print("=== EXTRA TEST SCENARIOS ===\n")

    acc = PersonalAccount(7777, "Test User")
    print("Initial:", acc)

    try:
        acc.withdraw(100)
    except ValueError as e:
        print("Expected error (withdraw without balance):", e)

    acc + 1000
    print("After +1000:", acc)

    acc.deposit(250)
    acc - 300
    acc.deposit(50)

    print("Balance after multiple operations:", acc.get_balance())

    try:
        acc.withdraw(5000)
    except ValueError as e:
        print("Expected error (too much withdrawal):", e)

    acc.set_account_holder("Updated User")
    acc.set_account_number(8888)

    print("After updating account info:", acc)

    acc.print_transaction_history()


if __name__ == "__main__":
    main()