# a program that tells us how many days, weeks, months
# we have left if we live until 90 years old👇

age = input("What is your current age? ")

# converting age to int
age_int = int(age)

# sub the age_int by 90 since it is focus age
years_remaining = 90 - age_int

# Calculating
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

print(message)
