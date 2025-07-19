princlple =0
rate=0
time=0

while princlple <= 0:
        princlple=float(input("Enter principle amount: "))
        if princlple <= 0:
            print("Priciple can not be less than zero")
print(princlple)
while rate <= 0:
        rate=float(input("Enter rate amount: "))
        if rate <= 0:
            print("rate can not be less than zero")
print(rate)
while time <= 0:
        time=int(input("Enter loan time in years: "))
        if time <= 0:
            print("loan time can not be less than zero")
print(rate)
total=princlple* pow(1+rate/100,time)
print(f" total amount  in years {time} is : $ {total:.2f}")