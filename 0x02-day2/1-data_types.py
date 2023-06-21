two_digit_number = input("Type a two digit number: ")

# We need to know the data type
print(type(two_digit_number))

# use str to locate index
First_Digit = two_digit_number[0]
Second_Digit = two_digit_number[1]

# convert str to int so it can get calculated
# str can not performe math 1+2 = 3
# str will only put them together as 12
result = int(First_Digit) + int(Second_Digit)
print(result)

###########################################
# different option without needing result
# print(int(First_Digit) + int(Second_Digit))
