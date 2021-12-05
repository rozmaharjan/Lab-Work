#WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
a=int(input("subject 1 marks: "))
b=int(input("subject 2 marks: "))
c=int(input("subject 3 marks: "))
d=int(input("subject 4 marks: "))
total = (a+b+c+d)
print(f"total: {total}")
avg = (a+b+c+d)/4
print(f"precentage:{avg}%")

if(avg>90):
    print("Congratulations! Your Grade is A")
elif(avg>=80 and avg<90):
    print("Congratulations! Your Grade is B")
elif(avg>=70 and avg<80):
    print("Congratulations! Your Grade is C")
elif(avg>60 and avg<70):
    print("Congratulations! Your Grade is D")
else:
    print("Sorry you have failed!")