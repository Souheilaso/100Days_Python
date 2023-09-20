# try:
#     with open("a_file.txt", "r") as file:
#         content = file.read()
#     dictionary_key = {"key": "value"}
#     print(dictionary_key["sdf"])
# except FileNotFoundError:
#     with open("a_file.txt", "w") as file:
#         file.write("new line\n")
# except KeyError as error_message:
#     print(f"the {error_message} key does not exist.")
# else:
#     print(content)
# finally:
#     print("The file is closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("human height should not be over 3 meters")
bmi = weight / height ** 2
print(bmi)
