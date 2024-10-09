# Make a program that reads the width and height of a wall in meters, calculates its area, and the amount of paint needed to paint it, knowing that each liter of paint covers an area of 2m²

height = float(input('What is the height of the wall? '))
width = float(input('What is the width of the wall? '))
area = height * width

print(f'Area of {area}')

liters_per_square_meter = 2
paint_needed = area / liters_per_square_meter

print(f'The amount of paint needed is {paint_needed}')
