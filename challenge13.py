# Make an algorithm that reads an employee's salary and shows their new salary, with a 15% increase

salary = float(input('Enter the employee\'s salary: R$'))
increase = 15 / 100  # 15% increase

new_salary = salary + (salary * increase)

print(f'The new salary, with a 15% increase, is: R${new_salary:.2f}')
