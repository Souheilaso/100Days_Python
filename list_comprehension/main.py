numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

# reminder
result = [n for n in numbers if n % 2 == 0]
print(result)
