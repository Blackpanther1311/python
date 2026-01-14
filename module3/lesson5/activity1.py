import random

playing=True
number=str(random.randint(10,20))

while playing:
    guess=input("giveme your best guss:")


    if number ==guess:
        print("you guessed the correct number")
        break
    else:
        print ("wrong answer please try again.")