import random
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("r")
        spaces.append("b")
    for i in range(2):
        spaces.append("g")
    return spaces

print(generate_wheel())
def spin_wheel(spaces):
    return random.choice(spaces)
print("Note: Use r for red, b for black, and g for green")        




def game():
    money = input("How much money do you want to start with? \n")
    spaces = generate_wheel()
    money = int(money)

    while True:
        

        bet = input("How much money do you want to lose-- sorry... bet? \n")
        bet=int(bet)
        color=input("What color do you want to bet on? \n")
        d=1
        d=random.randint(0,9)
        if d==0:
            d=0
            print("The wheel is spinning! Goooooooooooood luck")
            while d==0:
                d=0
                time.sleep(2)
                print("The wheel is still spinning! Goooooooooooood luck!")
                

        print("The wheel is spinning! Goooood Luck!")
        time.sleep(2)



        landed=spin_wheel(spaces)
        print("You have $" + str(money) + ".")
        print(landed)
        print("It landed on " + landed + ".")

        if landed==color:
            print("Congratulations! You guessed correctly! You won " + str(bet) + " dollars.")
            money=money+bet
            
        else:
            print("loser")
            money=money-bet
 
        print("You have " + str(money) + " dollars")

        z=input("Do you want to play again? Type yeah or nah \n")
        if z=="nah":
            print("coward")
            break


game()