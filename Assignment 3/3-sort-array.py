array = []
for i in range(5):
    x = int(input("please enter your number :"))
    array.append(x)
if array == sorted(array):
    print("Sorted✅")
elif array != sorted(array):
    print("Not sorted❌")    
    
print(array)    
