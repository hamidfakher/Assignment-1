import random

while True:
    dice = random.randint(1 , 6)
    if dice == 6:
        print("Your number is :",dice,"Well done, roll the dice again")
    else:
        print("Your number is :", dice)
        break
