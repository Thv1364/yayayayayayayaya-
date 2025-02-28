menu = {"Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def add_stuff(item, price):
    menu[item]=price

while True:
    want=input("What would you like to add?\n")
    want2=input("How much do you want it to cost?\n")
    add_stuff(want, want2)

    print("This is your menu: " + str(menu))
    a=input("Would you like to continue?\n")
    if a=="no" :
        break