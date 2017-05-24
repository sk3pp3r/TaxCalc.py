# TAX Calc Program by Haim Cohen 2017
# version 1.0
print("TAX Calculator version 1.0")
print("__________________________")
x = float(input("Enter price before tax: "))
y = float(input("Enter TAX rate (e.g 10%): "))
t = ((float(x)*float(y))/100)                   # function percent
print("__________________________")
print("base Price: " + repr(x) + " $")
print("Tax : " + str(y) + "%")
print("Tax is " + repr(t) + "$")
z = float(x)+float(t)
print("Total price include tax: " + repr(z) + "$")
print("__________________________")
print("### end of script ###")