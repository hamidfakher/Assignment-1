print ("Triangle Detection")

A = float(input("The first side of the triangle:"))
B = float(input("The second side of the triangle:"))
C = float(input("The third side of the triangle:"))


if B + C > A and C + A > B and A + B > C:
    print ("It is a triangle")    
else: 
    print ("Its not triangle")
