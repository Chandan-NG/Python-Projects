print("Hello World...!\nWelcome to the Tip Calculator\nLet's Calculate :)\n")

bill = float(input("What's the bill amount? $"))
tip_percent = int(input("What percentage of tip you want to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

total = bill + (bill * (tip_percent/100))
split = total / people

print(f"Each person should pay: ${round(split , 2)}")

print("Thank you...!")