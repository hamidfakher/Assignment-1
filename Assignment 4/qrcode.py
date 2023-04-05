import qrcode

name = input("please enter your first and last name :")
number = int(input("please enter your mobile number :"))

x = qrcode.make("name")
x.save("myqrcode.png")