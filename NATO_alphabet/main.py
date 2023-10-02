import pandas

data = pandas.read_csv("nato_alphabets.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabets")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()
