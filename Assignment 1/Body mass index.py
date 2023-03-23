weight = float(input("Please enter your weight:"))
height = float(input("Please enter your height:"))

bmi = weight / height ** 2

if bmi < 18.5:
    result = "Underweight"
elif bmi >= 18.5 and bmi <= 24.9 :
    result = "Normal weight"
elif bmi >= 25 and bmi <= 29.9 :
    result = "overweight"
elif bmi >= 30 and bmi <= 34.9 :
    result = "Obesity"
elif bmi >= 35 and bmi <= 39.9 :
    result = "Extreme Obesity" 

print(bmi ,result) 
