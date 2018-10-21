class BankAccount:

    def __init__(self, account_number, owner, balance):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []

    def __str__(self):
        return 'Owner: {} Account No: {} Balance ${:,.2f}'.format(
            self.__owner, self.__account_number, self.__balance
        )

    def get_account_number(self):
        return self.__account_number

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def set_owner(self, owner):
        self.__owner = owner

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append('Deposited ${:,.2f}'.format(amount))

    def withdrawal(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append('Withdrew ${:,.2f}'.format(amount))
        else:
            raise ValueError('Insufficient Funds')

    def transfer(self, other_account, amount):
        self.withdrawal(amount)
        other_account.deposit(amount)
