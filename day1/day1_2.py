print("  Welcome to the Tip Calculator")
print("---------------------------------")
bill = float(input("What was the total bill? $"))
tip_perc = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))
bill_per_person = ((bill * tip_perc / 100) + bill) / people
print(f"Each person should pay: ${bill_per_person:.2f}")
