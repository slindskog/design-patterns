import unittest
from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action: Action, amount: float):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.cmd_handlers = {
            Command.Action.DEPOSIT: self.deposit,
            Command.Action.WITHDRAW: self.withdraw
        }

    def process(self, command: Command) -> None:
        command.success = self.cmd_handlers[command.action](command.amount)

    def deposit(self, amount: float) -> bool:
        self.balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False


class Evaluate(unittest.TestCase):
    def test(self):
        a = Account()

        cmd = Command(Command.Action.DEPOSIT, 100)
        a.process(cmd)

        self.assertEqual(100, a.balance)
        self.assertTrue(cmd.success)

        cmd = Command(Command.Action.WITHDRAW, 50)
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertTrue(cmd.success)

        cmd.amount = 150
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertFalse(cmd.success)
