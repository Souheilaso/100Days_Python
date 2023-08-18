with open("my_file.txt") as file:
    content = file.read()
    print(content)
    file.close()

with open("my_file.txt", mode="a") as file:
    file.write("\n I am happy")

with open("new_file.text", mode="w") as file:
    file.write("Hello")
