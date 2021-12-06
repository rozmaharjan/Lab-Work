distance=4
velocity=25
t1=((distance/velocity)*60)
#bus stops at 10 places and spent 2 minutes
t2 =20
total1=t1 + t1
print(f"total time taken by bus is {total1}")

J1=((1/7)*60)
J2=((2/7)*60)
J3=((1/7)*60)
total2=J1+J2+J3
print(f"time taken by running is {total2}")
if (total1>total2):
    print ("running will be slower than by bus")
else:
    print("running will be fater than by bus")