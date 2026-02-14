from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Amount:
    """
    Represents a single transaction (deposit or withdrawal).
    """
    amount: float
    timestamp: datetime
    transaction_type: str  

    def __post_init__(self):
        if self.transaction_type not in ("DEPOSIT", "WITHDRAWAL"):
            raise ValueError("transaction_type must be 'DEPOSIT' or 'WITHDRAWAL'")
        if not isinstance(self.amount, (int, float)):
            raise TypeError("amount must be a number")
        if self.amount <= 0:
            raise ValueError("amount must be > 0")

    def __str__(self) -> str:
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"{ts} | {self.transaction_type:<10} | {self.amount:.2f}"


class PersonalAccount:
    """
    Personal bank account with basic operations and transaction history.
    """

    def __init__(self, account_number: int, account_holder: str):
        self._account_number = int(account_number)
        self._account_holder = str(account_holder)
        self._balance = 0.0
        self._transactions: List[Amount] = []

    def deposit(self, amount: float) -> None:
        amount = float(amount)
        tx = Amount(amount=amount, timestamp=datetime.now(), transaction_type="DEPOSIT")
        self._transactions.append(tx)
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be > 0")
        if amount > self._balance:
            raise ValueError("Insufficient funds: withdrawal exceeds current balance")

        tx = Amount(amount=amount, timestamp=datetime.now(), transaction_type="WITHDRAWAL")
        self._transactions.append(tx)
        self._balance -= amount

    def print_transaction_history(self) -> None:
        if not self._transactions:
            print("No transactions yet.")
            return

        print("--- Transaction History ---")
        for tx in self._transactions:
            print(tx)

    def get_balance(self) -> float:
        return self._balance

    def get_account_number(self) -> int:
        return self._account_number

    def set_account_number(self, account_number: int) -> None:
        self._account_number = int(account_number)

    def get_account_holder(self) -> str:
        return self._account_holder

    def set_account_holder(self, account_holder: str) -> None:
        self._account_holder = str(account_holder)

    def __str__(self) -> str:
        return (
            f"PersonalAccount(account_number={self._account_number}, "
            f"account_holder='{self._account_holder}', balance={self._balance:.2f})"
        )

    def __add__(self, amount: float) -> PersonalAccount:
        self.deposit(amount)
        return self

    def __sub__(self, amount: float) -> PersonalAccount:
        self.withdraw(amount)
        return self