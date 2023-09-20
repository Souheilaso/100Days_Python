try:
    file = open("a_file.txt")
    dictionary_key = {"key": "value"}
    print(dictionary_key["sdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("new line")
except KeyError as error_message:
    print(f"the {error_message} key does not exist.")
