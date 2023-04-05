import math

number = int(input("please enter your number :"))

List = []
for num in range (100):
    factorial = math.factorial(num)
    List.append(factorial)

if number in List:
    print("yes")    
else:
    print("no")    