# Write a Python program to sum three given integers. However, if two or more values are

# equal sum will be zero.

x=10
y=20
z=30
sum=x+y+z
if (x==y==z)or (y==z) or (x==z):
    print("sum is zero") 
else:
    print(sum)