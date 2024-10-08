# Create a program that reads how much money a person has in their wallet and shows how many Dollars they can buy

money_in_wallet = float(input('How much money do you have in your wallet? '))
dollar = money_in_wallet / 3.27

print(f'If you have R${money_in_wallet}, you can buy US${dollar:.2f}')
