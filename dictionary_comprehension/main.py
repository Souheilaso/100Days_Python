sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# converting  a sentence to a word
list_of_words = sentence.split()

new_dict = {word: len(word) for word in list_of_words}
print(new_dict)
