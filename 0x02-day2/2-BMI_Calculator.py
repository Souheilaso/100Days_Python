# a program that calculates the Body Mass Index
# (BMI) from a user's weight and height.👇

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Using the exponent operator **
BMI = int(weight) / float(height) ** 2

# converting BMI to an int
print(int(BMI))
