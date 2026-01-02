import pyttsx3
engine = pyttsx3.init()



age = int(input("Enter your Age = "))


if age < 18:
    print("Child")
elif age == 18:
    print("TeenAge")
elif age > 18:
    print("Adult")