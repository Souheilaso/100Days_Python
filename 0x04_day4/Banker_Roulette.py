# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

length = len(names)
# Generate a random index within the range
selection = random.randint(0, length - 1)

selected_person = names[selection]  # Get the name at the randomly chosen index

print(f"{selected_person} is going to buy the meal today!")
