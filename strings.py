# String methods

print("upper() :  The upper() method converts a string to upper case.")

name = "farhan khan"
print(name.upper(),"\n")





print("lower() : The lower() method converts a string to lower case.")

name = "FARHAN KHAN"
print(name.lower(),"\n")



print("strip() : The strip() method removes any white spaces before and after the string.")

name = "   Farhan khan     "
print(name.strip(),"\n")


print("rstrip() : The rstrip() removes any trailing characters.")

name = "Farhan khan !!!!"
print(name.rstrip("!"),"\n")



print("replace() : The replace() method replaces all occurences of a string with another string.")

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"),"\n")


print("split() : The split() method splits the given string at the specified instance and returns the separated strings as list items.")

str2 = "Silver Spoon"
print(str2.split(" "),"\n")      #Splits the string at the whitespace " ".


print("""Capitalize() : The capitalize() method turns only the first character of the string to 
      uppercase and the rest other characters of the string are turned to lowercase.
      The string has no effect if the first character is already uppercase.""")

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1 , "\n")

str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2 , "\n")




print("""center() : The center() method aligns the string to the center as per the parameters given by the user.""")

str1 = "Welcome to the Console!!!"
print(str1.center(50),"\n")


print("""We can also provide padding character. It will fill the rest of the fill characters provided by the user.""")
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."),"\n")


print("count() : The count() method returns the number of times the given value has occurred within the given string.")
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr,"\n")


print("endswith() : The endswith() method checks if the string ends with a given value. If yes then return True, else return False")

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"),"\n")

print("We can even also check for a value in-between the string by providing start and end index positions.")

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10),"\n")




print("""The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.""")


str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"),"\n")

print("""As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.""")

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"),"\n")


print("""The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then it raises an exception.""")

str1 = "He's name is Dan. He is an honest man."
print(str1.index("Dan"),"\n")

print("""As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.""")   

str1 = "He's name is Dan. He is an honest man."
# print(str1.index("Daniel"),"\n")   # Uncommenting this line will raise an exception   

print("""isalnum() : The isalnum() method checks if all the characters in the string are alphanumeric (either alphabets or numbers). If yes then return True, else return False.""")

str1 = "Hello123"
print(str1.isalnum(),"\n")

str2 = "Hello 123"
print(str2.isalnum(),"\n")

print("""isalpha() : The isalpha() method checks if all the characters in the string are alphabets. If yes then return True, else return False.""") 
str1 = "HelloWorld"
print(str1.isalpha(),"\n")

str2 = "Hello World"
print(str2.isalpha(),"\n")

print("""isdigit() : The isdigit() method checks if all the characters in the string are digits. If yes then return True, else return False.""")
str1 = "123456"
print(str1.isdigit(),"\n")

str2 = "1234abc"
print(str2.isdigit(),"\n")


print("""islower() : The islower() method checks if all the characters in the string are in lowercase. If yes then return True, else return False.""")
str1 = "hello world"
print(str1.islower(),"\n")

str2 = "Hello World"
print(str2.islower(),"\n")

print("""isprintable() : The isprintable() method checks if all the characters in the string are printable. If yes then return True, else return False.""")
str1 = "Hello World!"
print(str1.isprintable(),"\n")

str2 = "Hello\nWorld!"
print(str2.isprintable(),"\n")

print("""isspace() : The isspace() method checks if all the characters in the string are whitespaces. If yes then return True, else return False.""")
str1 = "   \t\n"
print(str1.isspace(),"\n")

str2 = "Hello World"
print(str2.isspace(),"\n")

print("""istitle() : The istitle() method checks if the string follows the rules of a title. If yes then return True, else return False.""")
str1 = "Hello World"
print(str1.istitle(),"\n")

str2 = "Hello world"
print(str2.istitle(),"\n")  


print("""isupper() : The isupper() method checks if all the characters in the string are in uppercase. If yes then return True, else return False.""")
str1 = "HELLO WORLD"
print(str1.isupper(),"\n")

str2 = "Hello World"
print(str2.isupper(),"\n")

print("""join() : The join() method takes all items in an iterable and joins them into one string.""")
myTuple = ("Farhan", "Khan", "is", "a", "developer")
str1 = " ".join(myTuple)
print(str1,"\n")

print("""The join() method can be used with different iterables like lists, sets, dictionaries etc.""")

myList = ["Python", "is", "awesome"]
str2 = "-".join(myList)
print(str2,"\n")

mySet = {"I", "love", "coding"}
str3 = " ".join(mySet)
print(str3,"\n")

myDict = {"name": "Farhan", "role": "developer"}
str4 = " | ".join(myDict)
print(str4,"\n")

print("""lstrip() : The lstrip() method removes any leading characters (spaces are the default leading characters to remove).""")
name = "   Farhan khan     "
print(name.lstrip(),"\n")

print("""We can also specify the leading characters to remove.""")
name = "!!!!Farhan khan!!!!"
print(name.lstrip("!"),"\n")    

print("""partition() : The partition() method searches for a specified string and splits the string into a tuple containing three elements.""")
str1 = "I love programming in Python"
partStr = str1.partition("programming")
print(partStr,"\n")


print("""rfind() : The rfind() method searches for the last occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.""")
str1 = "He's name is Dan. He is an honest man."
print(str1.rfind("is"),"\n")
print("""As we can see, this method is somewhat similar to the rindex() method. The major difference being that rindex() raises an exception if value is absent whereas rfind() does not.""")
str1 = "He's name is Dan. He is an honest man."
print(str1.rfind("Daniel"),"\n")    

print("""swapcase() : The swapcase() method converts uppercase characters to lowercase and lowercase characters to uppercase.""")   
str1 = "Hello World"    
print(str1.swapcase(),"\n")
str2 = "hELLO wORLD"
print(str2.swapcase(),"\n")

print("""title() : The title() method converts the first character of each word to upper case.""")
str1 = "hello world. welcome to the console."
print(str1.title(),"\n")
str2 = "HELLO WORLD. WELCOME TO THE CONSOLE."
print(str2.title(),"\n")
print("""zfill() : The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.""")
str1 = "Farhan"
print(str1.zfill(10),"\n")
str2 = "12345"
print(str2.zfill(8),"\n")

print("""format() : The format() method formats the specified value(s) and insert them inside the string's placeholder.""")
str1 = "Hello, {}. Welcome to the console."
print(str1.format("Farhan"),"\n")
str2 = "The {} is {} years old."
print(str2.format("car", 5),"\n")

