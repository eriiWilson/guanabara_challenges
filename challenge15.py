# Write a program that asks the number of kilometers driven by a rented car and the number of days it was rented.
# Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.

km_driven = float(input('Enter the number of kilometers driven: '))
days_rented = int(input('Enter the number of days the car was rented: '))

# Calculate the total cost
cost_per_day = 60
cost_per_km = 0.15

total_cost = (days_rented * cost_per_day) + (km_driven * cost_per_km)

print(f'The total amount to pay is: R${total_cost:.2f}')
