# Make an algorithm that reads the price of a product and shows its new price, with a 5% discount

price = float(input('Enter the price of the product: R$'))
discount = 5 / 100  # 5% discount

new_price = price - (price * discount)

print(f'The new price, with a 5% discount, is: R${new_price:.2f}')
