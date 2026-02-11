import random
import time

number = random.randint(1,100)

def intro():
    print("i am thinking of a number between1-100")

    if number%2==0:
        x='even'
    else:
        x='odd'

    print("the number is ",x)
    time.sleep(.5)
    print("guess the number")


def pick():
    count =0

    while count<6:
        time.sleep(.25)
        enter= input("guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                count=count+1
                if count<6:
                    if guess<number:
                        print ("too low")
                    if guess>number:
                        print("too high")
                    if guess!= number:
                        print("try again!")
                    if guess==number:
                        break
            if guess>100 or guess <1:
                print ("not in range " )
        except:
            print("the number is incorrect")

    if guess==number:
        print("good job! you guessed my number")
    if guess!=number:
        print("nope.the number i was thinking of was "+str(number))
playagain ="yes"
while playagain =="yes"or playagain=="y" or playagain=="Yes":
    intro()
    pick()
    print("do you want  to play again?")
    playagain=input()