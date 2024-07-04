from trading_account import TradingAccount
from user_information import User
import hashlib


users = []
password_data = {}


def user_registration(username, password):
    try:
        next(filter(lambda u: u.username == username, users))
        print("That username already exist.")

    except StopIteration:
        try:
            name = input("Enter your name:")
            email = input("Enter your e-mail address:")
            initial_money = float(input("Enter your starting amount"))
            trading_account = TradingAccount(initial_money)
            user = User(name, username, email, trading_account, password)
        except ValueError:
            return "Invalid information"

        users.append(user)
        password_data[user.username] = password
        return f"User with username '{username}' was successfully added"


def show_user_profile(current_user):
    result = []
    result.append(current_user.show_user_info())
    result.append(current_user.trading_account.show_account_info)
    return f"{result}"


def user_login(username, password):
    try:
        user = next(filter(lambda u: u.username == username, users))
        if password != password_data[username]:
            print("Invalid password!")
    except StopIteration:
        print('Invalid username!')
    return user


def change_password(username, old_password, new_password):
    try:
        user = next(filter(lambda u: u.username == username, users))
    except StopIteration:
        print('Invalid username!')

    if old_password != password_data[username]:
        print("Invalid password!")

    password_data[user] = new_password
    return "Password was successfully changed"


def hashing_password(plain_password):
    h = hashlib.new("SHA256")
    h.update(plain_password.encode())
    return h.hexdigest()


while True:
    print('Menu')
    print('1.User Registration')
    print('2.User Login')
    print('3.Change Password.')
    print('4.Exit')
    input_choice = input('Choose from the Menu and enter your choice:')
    if input_choice == '4':
        print('Goodbye!')
        break

    if input_choice != '1' and input_choice != '2' and input_choice != '3':
        print('Invalid choice!')
        print()

    else:
        input_username = input("Enter your username:")
        input_password = input("Enter your password:")
        input_password = hashing_password(input_password)
        if input_choice == '1':
            print(user_registration(input_username, input_password))
            print()

        elif input_choice == '2':
            if user_login(input_username, input_password):
                user = user_login(input_username, input_password)
                print(user.show_user_info())

                while True:
                    print('Menu')
                    print('1.Add new trade.')
                    print('2.Show account info.')
                    print('3.Exit')

                    choice = input('enter your choice: ')
                    if choice == '1':
                        input_amount = float(input("Enter amount: "))
                        try:
                            user.trading_account.add_new_trade(input_amount)
                            print(f"New trade ${input_amount} was successfully added")
                        except ValueError:
                            print("You left with nothing. Go find job!")

                    elif choice == '2':
                        print(user.trading_account.show_account_info())
                    elif choice == '3':
                        print('Goodbye!')
                        break
                    else:
                        print('Invalid choice!')
                        print()

        elif input_choice == '3':
            if user_login(input_username, input_password) is True:
                new_password = input("enter new password:")
                hashing_password(new_password)
                change_password(input_username, input_password, new_password)
                print('You successfully changed your password!')
                print()


