import math

print ("welcome to my calculator")


print ("+ = sum")
print ("- = sub")
print ("* = mul")
print ("/ = div")
print ("sin")
print ("cos")
print ("tan")
print ("cot")
print ("sqrt")
print ("fac")
print ("log")
print ("please enter your choice:")
op = input()
if op == "+" or op == "-" or op =="*" or op == "/":  
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))
elif op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "sqrt" or op == "fac" or op == "log":
    a = float(input("enter first number:"))
if op == "+":
    result = a + b
    print (result)
elif op == "-":
     result = a - b 
     print (result)
elif op == "*":
     result = a * b
     print (result)
elif op == "/":
    if b == 0:
        result = "cannot divide by zero" 
        print (result)
    else:
        result = a / b 
elif op == "sin":
    result = math.sin(a)
    print (result)
elif op == "cos":
    result = math.cos(a)
    print (result)
elif op == "tan":
    result = math.tan(a)
    print (result)
elif op == "cot":
    result = math.cot(a)
    print (result)
elif op == "sqrt":
    if a > 0 :
        result = math.sqrt(a)
        print (result)
    else:
        print ("Cannot enter zero")
elif op == "fac":
    result = math.factorial(a)
    print (result)        
elif op == "log":
    result = math.log(a)
    print (result)

 