userAge = int(input("Please enter your age: "))

if(userAge <= 13):
    print("Child !")
elif(userAge > 13 and userAge <= 19):
    print("Teenager !")
elif(userAge >= 20 and userAge <= 59):
    print("Adult !")
else:
    print("Senior !")