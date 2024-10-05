print('''╔═.✵.══════════╗
 operators
╚══════════.✵.═╝''')

num1 = int(input('Type a number so we can do some arithmetic operations '))
num2 = int(input('type Type another number. '))
addition = (num1 + num2)
subtraction = (num1 - num2)
multiplication = (num1 * num2)
division = float(num1 / num2)
integer_division  = (num1 // num2)
modulo = (num1 % num2)
exponentiation = (num1 ** num2)

print(f'The calculation {num1} + {num2} equals {addition}')
print(f'The calculation {num1} - {num2} equals {subtraction}')
print(f'The calculation {num1} * {num2} equals {multiplication}')
print(f'The calculation {num1} / {num2} equals {round(division ,2)}')
print(f'The calculation {num1} // {num2} equals {integer_division}')
print(f'The remainder of the division {num1} % {num2} equals {modulo}')
print(f'The calculation {num1} ** {num2} equals {exponentiation}')

