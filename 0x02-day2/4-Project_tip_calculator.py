# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n"))

pertentage = int(input(
    "What percentage tip would you like to give? 2, 5, 10, or anything you want?\n"))

people = int(input("how many people to split the bill?\n"))

tip_plus_bill = bill * (pertentage / 100) + bill
tip_per_person = tip_plus_bill / people
final = round(tip_per_person, 2)

print(f"Each person should pay: {final}")
