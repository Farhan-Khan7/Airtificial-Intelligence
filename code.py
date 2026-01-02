import pyttsx3
engine = pyttsx3.init()



# age = int(input("Enter your Age = "))


# if age < 18:
#     print("Child")
# elif age == 18:
#     print("TeenAge")
# elif age > 18:
#     print("Adult")

# username = input("Enter Username : ")
# password = input("Enter Password : ")

# if(username == "admin" and password == "pass"):
#     print("Login Successfully !")
# elif(username != "admin"):
#     print("Username Wrong !")
# else:
#     print("Wrong Password !")

word = "Artificial Intelligence"
count = 0
for ch in word:
    if(ch == 'i'):
        count += 1

print("Total Words =", count)