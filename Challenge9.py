# Make a program that reads any integer and displays its multiplication table on the screen.

number = int(input('Write a number: '))

# Display the multiplication table (simplified version)
print(f'{number * 1}\n{number * 2}\n{number * 3}\n{number * 4}\n{number * 5}\n{number * 6}\n{number * 7}\n{number * 8}\n{number * 9}\n{number * 10}')

# Display each multiplication step
print(f'{number} x 1 = {number * 1}')
print(f'{number} x 2 = {number * 2}')
print(f'{number} x 3 = {number * 3}')
print(f'{number} x 4 = {number * 4}')
print(f'{number} x 5 = {number * 5}')
print(f'{number} x 6 = {number * 6}')
print(f'{number} x 7 = {number * 7}')
print(f'{number} x 8 = {number * 8}')
print(f'{number} x 9 = {number * 9}')
print(f'{number} x 10 = {number * 10}')

# Using a loop to display the multiplication table
for number2 in range(1, 11):
    print(f'{number} x {number2} = {number * number2}')


#just a little test haha
'''numeros = (1, 2, 3, 4)
for numeros2 in range (1, 5):
    (print(numeros))'''