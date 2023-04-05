list1 = []

number = int(input("enter length of your list :"))
for i in range(number):
    list1.append(int(input("please enter your number:")))

print("your list:" , list1)    
print("your reverse list:" , set(list1))
