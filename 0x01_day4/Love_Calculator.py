# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

names = name1.lower() + name2.lower()

counter1 = names.count("t") + names.count("r") + \
    names.count("u") + names.count("e")
counter2 = names.count("l") + names.count("o") + \
    names.count("v") + names.count("e")

score = str(counter1) + str(counter2)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
