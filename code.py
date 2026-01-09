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




# studentInfo = {
#     "student1" : "Farhan khan",
#     "stdmarks1" : 85,
# }

# keys = studentInfo.keys()
# values = studentInfo.values()

# print("A - Add a student")
# print("B - Update marks")
# print("C - Search for a student")
# print("D - Display all students and marks")


# operation = input("What do you want : ")

# if(operation == 'A'):
#     studentInfo.update({
#         input("Enter key name ") : input("Enter value of key ")
#     })
#     operation = input("What do you want : ")
# elif(operation == 'B'):
#     studentKey = input("Enter student key to update marks ")
#     if studentKey in keys:
#         studentInfo[studentKey] = int(input("Enter new marks "))
#     else:
#         print("Student not found ")
# elif(operation == 'C'):
#     studentKey = input("Enter student key to search ")
#     if studentKey in keys:
#         print(f"{studentKey} : {studentInfo[studentKey]}")
#     else:
#         print("Student not found ")
# elif(operation == 'D'):
#     for key in keys:
#         print(f"{key} : {studentInfo[key]}")


# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]

# unique_students = set()

# for name,courses in info:
#     if courses == "English":
#         print(name)




# i = 1
# while i < 50:
#     if i%2==0:
#         print(i)
#     i+=1


# x =int(input("entr a number : "))
# count = 0 
# if x == 0 :
#     count = 1
# else :
#     x = abs(x)
#     while x!= 0 :
#         x//= 10
#         count+=1
# print(f"number has {count} digits")





# x = int(input("Enter a number"))
# count = 0
# if x == 0:
#     count = 1
# else:
#     x = abs(x)
#     while x != 0:
#         x //= 10
#         count += 1
# print(f"Number has {count} digits")



# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1




# no = int(input("Enter the no"))
# temp = no
# reverse_no = 0
# last_digit = 0
# while no > 0:
#     last_digit = no % 10
#     reverse_no = reverse_no * 10 + last_digit
#     no //= 10

# if reverse_no == temp:
#     print("Palindrom no")
# else:
#     print("Not palindrom no")






# x = int(input("Enter a number"))
# for i in range(x):
#     for j in range(x):
#         print("*", end = " ")
#     print()




# no1 = int(input("Enter 1st no"))
# no2 = int(input("Enter 2nd no"))
# i = no1
# while i % no2 != 0:
#     i += no1
# print(f"{i} is LCM")















# x = int(input("Enter the no"))
# if x <= 1:
#     print("not a prime")
# else:
#     i = 2
#     isprime = True
#     while i < x:
#         if x % i == 0:
#             isprime = False
#             break
#         i += 1
    
#     if isprime:
#         print("prime no")
#     else:
#         print("Not prime")


# x = 100
# for i in range(2, x):
#     isprime = True
#     for j in range(2, i):
#         if i == 2:
#             pass
#         elif i % j == 0:
#             isprime = False
#             break
#     if isprime:
#         print(i)




# x = 100
# for i in range(2, x):
#     isprime = True
#     for j in range(2, i):
#         if i == 2:
#             pass
#         elif i % j == 0:
#             isprime = False
#             break
#     if isprime:
#         print(i)



# x = int(input("Enter a no"))
# i = 1
# while i <= x:
#     if x % i == 0:
#         print(i)
#     i += 1









# x = int(input("Enter the number"))
# if x < 0:
#     print("Not an armstrong no")
# else:
#     digit_count = 0
#     digit = x
#     while digit > 0:
#         digit //= 10
#         digit_count += 1
    
#     temp = x
#     last_digit = 0
#     sum = 0
#     while x > 0:
#         last_digit = x % 10
#         sum = sum + last_digit ** digit_count
#         x //= 10
        
#     if temp == sum:
#         print("Armstrong no")
#     else:
#         print("Not armstrong")



















x = int(input("Enter the no"))
pow = int(input("Enter the pow"))
result = 1
for i in range(1, pow + 1):
    result *= x
print(result)

















# s = "I love python"
# p = s.replace("python", "Java")
# print(p)
# a = "Hello"
# b = "world"
# c = a + b
# print(c)



# s = input("Enter a word")
# count = 0
# for ch in s.lower():
#     if ch in "aeiou":
#         count += 1
# print(count)



# s = input("Enter string")
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)



# s = input("Enter sentence: ")
# print(" ".join(s.split()[::-1]))
# arr = [10, 20, 30, 40, 50]
# arr = list(set(arr))
# arr.sort()
# print(arr[-2])



# n = int(input("Enter number: "))
# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10
# print(sum)


# arr = [1, 2, 3, 4, 5, 6]
# even = odd = 0
# for i in arr:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even:", even)
# print("Odd:", odd)



# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]
# print(list(set(l1) & set(l2)))



# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d1.update(d2)
# print(d1)



# n = int(input("Enter a number"))
# print("Even" if n % 2 == 0 else "odd")