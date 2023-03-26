n1 = int(input("please enter first number :"))
n2 = int(input("please enter second number :"))
bmm = 0
if n1 > n2 :
    x = n2
else:
    x = n1
for i in range(1 , x +1):
    if(n1 % i == 0 ) and (n2 % i == 0) :
        bmm = i
kmm = int((n1 * n2) /bmm)
print("kmm = " , kmm)               