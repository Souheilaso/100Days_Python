print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_s = 2
Pepperoni_m_l = 3
Cheese = 1


if size.upper() == "S":
    if add_pepperoni.lower() == "Y":
        if extra_cheese.lower() == "Y":
            print("Your total bill is ", small_pizza + pepperoni_s + Cheese)
        else:
            print("Your total bill is ", small_pizza + pepperoni_s)
    else:
        print("Your total bill is ", small_pizza)
else:
    print("choose the right size again please")
