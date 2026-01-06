# import pyttsx3
# engine = pyttsx3.init()



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

# word = "Artificial Intelligence"
# count = 0
# for ch in word:
#     if(ch == 'i'):
#         count += 1

# print("Total Words =", count)

# sum = 0
# for i in range(1, 6, 1):
#     sum += i;

# print("sum = ", sum)


# def average(x, y , z):
#     avg = (x+y+z)/3
#     return avg

# x = int(input("Enter the value of X = "))
# y = int(input("Enter the value of Y = "))
# z = int(input("Enter the value of Z = "))

# ans = average(x , y , z )
# print("Average of x y z = ", ans)


# def NetSalary(salary , tax):
#     tax = (salary * tax)/100
#     sal = salary - tax
#     return tax , sal

# salary = int(input("Enter your salary = "))
# tax = int(input("which percentage add tax on your salary "))

# NetSalary = NetSalary(salary , tax)

# print("Your Net Salary " , NetSalary)



# a = int(input("Enter a = "))
# b = int(input("Enter b = "))

# for i in range(a , b):
#     if(i%2 == 0):
#         print(i)
#     elif(i%2 != 0):
#         continue


# num = 312
# rev = 0
# counter = 0

# while num > 0:
#     digit = num % 10
#     counter += 1
#     rev = rev * 10 + digit
#     num = num // 10
# print("total digits = ", counter)
# print(rev)


# str = input("Enter string = ")
# reverse = ""
# for val in str:
#     reverse = val + reverse

# if(str == reverse):
#     print("It is palindrome ".format(reverse))
# elif(str != reverse):
#     print("It is not palindrome ")



# a = 10
# b = 5

# print(f"sum of {a} & {b} is {a + b}")

# list1 = [1, 2, 7]
# list2 = [2, 4, 5]

# list1.extend(list2)
# list1.sort()
# print(list1)


# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# evenTuple = []
# oddTuple = []

# for val in tup:
#     if(val%2 == 0):
#         evenTuple.append(val)
#     elif(val%2 != 0):
#         oddTuple.append(val)

# print(tuple(evenTuple))
# print(tuple(oddTuple))


# interger = int(input("Enter interger Number = "))

# for i in range(interger):
#     print("Hello World")


# n = int(input("Enter any natural number = "))
# for i in range(n+1):
#     if i<=n:
#         print(i)

# n = int(input("Enter any natural number = "))

# for i in range(n,0,-1):
    # print(i)


# n = int(input("Enter any natural number = "))

# for i in range(1, n+1):
#     print(f"{n} x {i} = {i*n}")

studentInfo = {
    "student1" : "Farhan khan",
    "stdmarks1" : 85,
}

print("A - Add a student")
print("B - Update marks")
print("C - Search for a student")
print("D - Display all students and marks")


operation = input("What do you want : ")

if(operation == 'A'):
    studentInfo.update({
        input("Enter key name ") : input("Enter value of key ")
    })

print(studentInfo)