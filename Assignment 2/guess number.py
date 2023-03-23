import random

computer_number = random.randint(10,40)
x = 0
while True :
    user_number = int(input())
    x = x + 1
    if computer_number == user_number:
        print("barikala")
        print("you win")
        print("✅")
        break
    elif computer_number > user_number:
        print("boro bala") 
        print("go up") 
        print("⬆️")
    elif computer_number < user_number:
        print("bia paeen")
        print("go down")
        print("⬇️")
print("Tedade hads haye shoma = " , x)        

