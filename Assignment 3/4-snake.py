
array = []
array2 = []
n = int(input("please enter length of snake :"))

for i in range(n):
    array.append(i + 1)
    if i % 2 == 0 :
        array2.append("*")
    else:
        array2.append("#")    

print(array2)    
