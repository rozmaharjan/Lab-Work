#Given a positive real number, print its fractional part
import math
x=int(input("enter any number: "))
a,b= math.modf(x)
print(a)
print(b)