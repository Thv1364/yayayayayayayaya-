import os
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]


while True:
    a=input("What item would you like to remove from the list? Type stop to get out of here. Type STOP to really get out of here. \n")
    
    if a=="stop":
        print("You end with: ")
        print(groceries)
        break
    elif a=="STOP":
        os.system('shutdown now -h')
        break

    else:
        groceries.remove(a)
        print("You have: ")
        print(groceries)