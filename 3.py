import os
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
b=7

while True:
    if b<=0:
        print("You are out of stuff")
        break
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
        b=b-1
        print("You have: ")
        print(groceries)