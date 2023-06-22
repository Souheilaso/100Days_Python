# This is a program that can spot even and odd numbers 👇
number = int(input("Which number do you want to check? "))

# even numbers don't have reminders (0)
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
