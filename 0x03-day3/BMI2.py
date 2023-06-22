weight = int(input("What is your weight? "))
height = float(input("what is your height? "))

BMI = weight / (height ** 2)
result = round(BMI)

if BMI < 18.5:
    print("you are underweight")
elif BMI < 25:
    print("You have a normal weight")
elif BMI < 30:
    print("You are slightly overweight")
elif BMI < 35:
    print("You are slighly Obese")
else:
    print("You are clinically Obese")
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
