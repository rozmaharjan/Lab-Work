# #Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else

# print ‘COMMON YEAR’.

# Hint: • a year is a leap year if its number is exactly divisible by 4 and is not

# exactly divisible by 100

# • a year is always a leap year if its number is exactly divisible by 400
x=int(input("enter a year"))
if (x%4==0 and x%100 !=0 or x%400==0):
    print("LEAP YEAR")
else:
    print("COMMON YEAR")    