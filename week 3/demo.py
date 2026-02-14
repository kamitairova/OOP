from personal_account import PersonalAccount

def main():
    acc = PersonalAccount(1001, "Kamilla Tairova")
    print(acc)

    acc.deposit(500)
    acc.withdraw(120)

    acc + 200
    acc - 50

    print("\nBalance:", acc.get_balance())
    acc.print_transaction_history()

    print("\nFinal:", acc)

if __name__ == "__main__":
    main()