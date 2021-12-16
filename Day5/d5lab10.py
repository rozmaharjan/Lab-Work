#Write a Python program that accepts a string and calculate the number of digits and letters
x = input("Input a string : ")
d=l=0
for c in x:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)