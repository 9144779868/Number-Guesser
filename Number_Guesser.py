import random
from playsound import playsound
import time

comp_number = random.randint(0, 99)

print("Type 'yes' to play sounds and 'no' to not")
time.sleep(1)

sound_permission = input("Play sounds ? : ")
chances = 5

time.sleep(1)
if (sound_permission.capitalize() == "Yes") :
    print("Sound effects will be played!")
else :
    print("Sound effects will not be played!")

time.sleep(1)

while (True) :
    user_number = int(input("Please enter the number here : "))
    time.sleep(1.2)
    if (user_number == comp_number) :
        print("YEAAAA! You have guessed the number right")
        if (sound_permission.capitalize() == "Yes") :
            playsound("victory.mp3")
        break

    elif (user_number > comp_number) :
        print("OHNOO! The actual number is smaller than "+str(user_number))

    elif (user_number < comp_number) :
        print("OHNOO! The actual number is greater than "+str(user_number))
    
    chances -= 1

    if (chances == 0) :
        print("OHNOO! You lost the game... better luck next time")
        print("The actual number was",comp_number)
        playsound("lose.mp3")
        break

    time.sleep(1)
    print(chances,"chances are left")