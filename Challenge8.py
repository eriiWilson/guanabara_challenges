# Write a program that reads a value in meters and displays it converted to centimeters and millimeters
meters_value = float(input('Enter a measurement in meters: '))
centimeters = meters_value * 100
millimeters = meters_value * 1000

print(f'The value in meters {meters_value}m converted to centimeters is {centimeters}cm and to millimeters is {millimeters}mm')
