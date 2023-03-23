sum_sec = 0 
hour = float(input("Please enter hour :"))
minute = float(input("please enter minute :"))
second = float(input("please enter second :"))
sum_sec = hour * 3600
sum_sec = ( minute * 60) + sum_sec
sum_sec = second + sum_sec
print(sum_sec)
