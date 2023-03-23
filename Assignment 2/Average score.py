sum = 0
score_counter = 0
print("Write exit for calculation average")
while True:
    score = input("Please enter your score:")
    if score == "exit":
        break

    else:
        sum = float(score) + sum 
        score_counter = score_counter + 1

print("Average score is :", sum / score_counter)        
