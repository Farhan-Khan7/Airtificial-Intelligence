import pyttsx3
engine = pyttsx3.init()



x = int(input("Enter value of x = "))
y = int(input("Enter value of y = "))
z = float(input("Enter value of z = "))


avg = float((x+y+z)/3)

print(type(avg))

# print("Sum = " , x+y)
# print("Difference = " , x-y)
# print("product = " , x*y)
# print("quotient = ", x/y)