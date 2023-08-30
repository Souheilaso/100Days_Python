numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

# reminder
result = [n for n in numbers if n % 2 == 0]
print(result)

# reading both files then finding similar numbers and creating a list
with open("file1.txt") as data_file1:
    content1 = data_file1.read()

with open("file2.txt") as data_file2:
    content2 = data_file2.read()

list_1 = [int(number) for number in content1.split()]
list_2 = [int(number) for number in content2.split()]
similarities_list = [same_num for same_num in list_1 if same_num in list_2]
print(f"Similar numbers from file1 and file2 are: {similarities_list}")
