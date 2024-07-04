import re

from trading_account import TradingAccount


class User:
    def __init__(self, name, username, mail, trading_account: TradingAccount, password):
        self.name = name
        self.username = username
        self.mail = mail
        self.trading_account = trading_account
        self.password = password
        self.trading_count = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 3:
            raise ValueError("Name cannot be less than 4 characters!")
        self.__name = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) <= 3:
            raise ValueError("Username cannot be less than 4 characters!")
        self.__username = value

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        pattern = r'[A-Za-z]{3,}[-.]*[a-z]*@[a-z]+.[a-z]+'
        result = re.findall(pattern, value)
        if not result:
            raise ValueError("Invalid e-mail address!")
        self.__mail = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 symbols!")
        self.__password = value

    def show_user_info(self):
        return f"Hello {self.name}"