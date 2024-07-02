trades = []
bank_money = float(input('Enter you Bank Account Qanttity: '))

count = int(input('Please enter the number of trades: '))
trades_sum = 0
for trade in range(count):
    money = float(input('Please enter the gain ot loss '))
    date = input('Please enter trading date in format "DD-MM-YY"')

    bank_money += money

    if bank_money <= 0:
        print('You lost everything you had. Go find job!')

    trades_sum += money

    trades.append([money, date])

average_sum = trades_sum // count

print(f'Your average trade results are: {average_sum:.2f}')

[print(f'trade results: {trades[row][0]} , trade date: {trades[row][1]}') for row in range(len(trades))]
print(f'Your current bank account: {bank_money:.2f}')

