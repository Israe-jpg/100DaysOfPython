print("Welcome to the tip Calculator")
totallBill = float(input("What was the total Bill?$"))
percentageTip = float(input("How much tip would you like to give? 10, 12, 15? "))
numbOfPeople = float(input("How many people to split the bill?"))

if percentageTip == 10:
    print(f"Each person should pay: ${(totallBill * 1.10 / numbOfPeople ):.2f}")
elif percentageTip == 12:
   print(f"Each person should pay: ${(totallBill * 1.12 / numbOfPeople ):.2f}")
elif percentageTip == 15:
    print(f"Each person should pay: ${(totallBill * 1.15 / numbOfPeople ):.2f}")
else:
    print("Error")

 