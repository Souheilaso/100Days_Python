with open("/Users/sue/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
    file.close()

with open("/Users/sue/Desktop/my_file.txt", mode="a") as file:
    file.write("\ntesting absolute path")

with open("new_file.text", mode="w") as file:
    file.write("Hello")
