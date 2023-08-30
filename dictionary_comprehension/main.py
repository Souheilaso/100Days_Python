sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# converting  a sentence to a word
list_of_words = sentence.split()

new_dict = {word: len(word) for word in list_of_words}
print(new_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {days: temperature * 9/5 + 32 for (days, temperature) in weather_c.items()}

print(weather_f)
