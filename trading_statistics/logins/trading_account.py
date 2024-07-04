class TradingAccount:
    def __init__(self, amount=0):
        self.amount = amount
        self.trades_count = 0

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Your bank amount cannot be negative!")
        self.__amount = value

    def add_new_trade(self, amount):
        self.trades_count += 1
        self.amount += amount

        return "Trade was successfully added!"

    def show_account_info(self):
        average = self.amount / self.trades_count
        return f"Account amount: ${self.amount:.2f}\nTrades: {self.trades_count}\nAverage: {average:.2f}"


