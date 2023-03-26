import random
array = []
x = 0

while len(array) < n :
    n = int(input("please enter number of array :"))
    x = random.randint(0 , n + 100 )
    if x not in array :
        array.append(x)

print(array)
