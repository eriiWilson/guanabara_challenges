# Create an algorithm that reads a number and shows its double, triple, and square root
import math

n1 = int(input('write a number '))
d = (n1 *2)
t = (n1 *3)
sr = (math.sqrt(n1))

print(sr)
print(d)
print(t) 

#other ways to show square root
sr = n1 ** (1/2)
print(sr)

sr = pow(n1, 1/2)
print(sr)