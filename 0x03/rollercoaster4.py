print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
picture = input("Do you want to take a rollercoaster picture? Yes / No\n")
# prices
picture_price = 3
kids_ticket = 5
teens_ticket = 7
adult_ticket = 12
# code
if height >= 120:
    if age < 12:
        if picture.lower() == "yes":
            print(
                f"Your Ticket price is ${kids_ticket + picture_price}.Enjoy your ride.")
        else:
            print(f"Your ticket price is ${kids_ticket}.Enjoy your ride.")
    elif age <= 18:
        if picture.lower() == "yes":
            print(
                f"Ticket price is ${teens_ticket + picture_price}.Enjoy your ride.")
        else:
            print(f"Your ticket price is ${teens_ticket}.Enjoy your ride.")
    else:
        if picture.lower() == "yes":
            print(
                f"Ticket price is ${adult_ticket + picture_price}.Enjoy your ride.")
        else:
            print(f"Your ticket price is ${adult_ticket}.Enjoy your ride.")
else:
    print("Try again next year!")
