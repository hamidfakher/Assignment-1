n = int(input("please enter number of fibo :"))
n1 = 1
n2 = 0
for i in range(n):
    sum = n1 + n2
    n1 = n2
    n2 = sum
    print(sum)
