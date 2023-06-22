"""
This is a program that checks reminders
Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

"""

number = int(input("Which number do you want to check? "))
calculation = number % 2

if calculation == 0:
    print(f"it is even with {calculation} reminder")
else:
    print(f"it is odd with a reminder of {calculation}")
