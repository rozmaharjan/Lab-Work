# convert seconds to day, hours and seconds.
s=int(input("Enter the value for second:"))
Day=(((s/60)/60)/60)
print(f"total day for given seconds: {Day}")
hour=((s/60)/60)
print(f"total day for given seconds: {hour}")
minute=(s/60)
print(f"total day for given seconds: {hour}")
