print("welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10 , 12 , 15"))
people = int(input("how many people to split the bill ? "))
bill_with_tip = bill * (1 + tip / 100)
print(bill_with_tip)