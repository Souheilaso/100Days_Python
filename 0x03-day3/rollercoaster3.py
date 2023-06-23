print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("your ticket price is $5")
    elif age <= 18:
        print("Your ticket price is $7")
    else:
        print("your ticket price is $12")
else:
    print("Try again next year!\n")
