classes=int(input("enter the number of classes held:"))
attended=int(input("enter the number of classes attended:"))
attendance=(attended/classes)*100
if attendance>=75:
    print("you are allowed to sit in exam")
else:
    print("sorry you are not elligible")
