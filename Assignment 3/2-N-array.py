import random
array = []
x = 0
n = int(input("please enter number of array :"))

while len(array) < n :
    x = random.randint(0 , n + 100 )
    if x not in array :
        array.append(x)

print(array)
