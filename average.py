print ("Average score")

name = input("Please enter your first name:")
family = input("Please enter your last name:")
score1 = int(input("Please enter your first score:"))
score2 = int(input("Please enter your second score:"))
score3 = int(input("Please enter your third score:"))
avg = ( score1 + score2 + score3 ) / 3
print (avg)
if avg >= 17 :
    print (name , family , "Your score are Great")
if 17 > avg >= 12 :
    print (name , family , "Your score are Normal")
if avg < 12 :
    print (name , family , "You failed")
    

  