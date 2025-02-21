import random
a=0
b=0
counter=0

random_num=random.randint(0,100)

while a==0:
    
    if b==1:
        guess= input("guess a number this time you idiot \n")
    if b==2:
        guess= input("guess a number this time you idiot! A NUMBER YOU INBECILE!! \n")
    if b==3:
        guess= input("guess a number this time you idiot! A NUMBER YOU INBECILE!! A NUMBER YOU COCKALORUM!!! \n")
    if b==4:
        guess= input("guess a number this time you idiot! A NUMBER YOU INBECILE!! A NUMBER YOU COCKALORUM!!! A NUMBER YOU NINNYHAMMER!!!! \n")
    if b==5:
        print("I don't have time for people like you. Go hide under a rock or whatever you are capable of doing \n")
        break
    if b==0:
        guess = input("guess a number \n")


    if guess.isnumeric() == False:
        print("Put a number you idiot \n\n\n\n\n")
        counter=counter+1
        b=b+1
        
    else:
        guess=int(guess)
        if guess < random_num:
            print("\nthe number you want is higher")
            counter=counter+1
            print(f"Guesses: {counter}" + "\n")
            #print("Guesses: "+ str(counter))
        elif guess > random_num:
            print("\nthe number you want is lower")
            counter=counter+1
            print("Guesses: " + str(counter) + "\n")
        else:
            counter=counter+1
            print("\ncongrats! get a life")
            print("Guesses: " + str(counter) + "\n")
            a=1
    print("___________________________________________")