#WAP sum of two numbers
# a = 1
# b = 2
# print(a+b)

#WAP find remainder when no. is divided by z.
# a = 34
# b = 5
# print("remainder when a is divided by b is", a %b)

#WAP to check the type of variables assigned using input()funtion
# a =  input("enter the value of a : ")
# print(type(a))

#use comparison operator to find wether a given variable is greater than 'b' or not.
# a = int(input("enter no. 1 :"))
# b = int(input("enter no. 2: "))
# print("a is greater than b is ",a>b)

#WAP to find avaerage of two no.s 
# a = int(input("enter no. 1 :"))
# b = int(input("enter no. 2: "))
# print("the average of these two numbers is:", (a+b)/2)

 # WAP to find square of a number
# a = int(input("enter no. 1 :")) 
# b = int(input("enter no. 2: "))
# print("square of a numbers is:",a*a) #a**2

#WAP to display a user enmarks here followed by good afternoon using input() functmarks here = input("entermarks here :")
# print(f"good aftermarks here} ")

#WAP to dimarks here and date
# letter = '''Dmarks here|>, 
# you are selected ! 
# <|date|>'''
# print(letter.replamarks here|>","aditi").replace("<|date|>", "20 march,2030"))

#WAP to detect double space in a strimarks here = "  aditi is a    good    girl and  "
# marks here.find("  ")) # strings  are immutable wich means you cannot change while executing


#WAp to store seven
# marks in a list
#
# marks =  []
# f1 = input("enter marks here: ")
# marks.append(f1) 
# f2 = input("enter marks here: ")
#
# marks.append(f2) 
# f3 = input("enter marks here: ")
#
# marks.append(f3) 
# f4 = input("enter marks here: ")
#
# marks.append(f4) 
# f5 = input("enter marks here: ")
#
# marks.append(f5) 
# f6= input("enter marks here: ")
#
# marks.append(f6) 
# f7 = input("enter marks here: ")
#
# marks.append(f7) 
# print(marks)

#WAP to accept marks of 6 students and display them in sorted manner
# marks = []
# f1 = int(input("enter marks here: "))
# marks.append(f1) 
# f2 = int(input("enter marks here: "))
# marks.append(f2) 
# f3 = int(input("enter marks here: "))
# marks.append(f3) 
# f4 = int(input("enter marks here: "))
# marks.append(f4) 
# f5 = int(input("enter marks here: "))
# marks.append(f5) 
# f6= int(input("enter marks here: "))
# marks.append(f6) 
# f7 = int(input("enter marks here: "))
# marks.append(f7) 

# marks.sort()
# print(marks)

#WAP check that a type cannot be changedin pythoon
# a = (23,34,45,"aditi")
# a[2]  "dditi"

#WAP to sum a list with 4 numbers
# l = (23,45,897,76)
# print(sum(l))

#WAP to count the no. of zeros in tuple
# a = (3,0,4,0,0,0,0,5,)
# n = a.count(0)
# print(n)
#5 
#1. WAP to cerste a dictionary of hindi words with values as thier english translation 
# words = {
#     "madad": "help", "kursi": "chair", "billi": "cat"
#     }
# word = input("enters the word you want meaning of:" )
# print(words[word])

# WAp to input 8 no. from user and display all unique number
# s = set()
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))

# print(s)

#can a set with 18(int) and"18"(str)as a value in it?
# s = set()
# s.add(18)
# s.add("18")
# print(s)

#s = {} what is the type of's'
# s = {}
#print(type(s))

# create an empty dict. allow 4 friends to enter their fav language as value and use key as their names
# d = {}

# name = input("enter friend name: ")
# lang = input("enter language name: ")
# d.update({name:lang})
# name = input("enter friend name: ")
# lang = input("enter language name: ")
# d.update({name:lang})
# name = input("enter friend name: ")
# lang = input("enter language name: ")
# d.update({name:lang})
# name = input("enter friend name: ")
# lang = input("enter language name: ")
# d.update({name:lang})
# print(d)

# a = int(input("enter a number: "))

# if(a>=18):
#     print("yes ")
# else:
#     print("no")

# CONDITIONAL STATEMENT PRACTICE 

# a1 = int(input("enter number 1: "))
# a2 = int(input("enter number 2: "))
# a3 = int(input("enter number 3: "))
# a4 = int(input("enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print(" Greatest number is a1: ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print(" Greatest number is a2: ",a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print(" Greatest number is a3: ",a3)

# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number is a4: ", a4)


#WAP to detect a spam comments
# p1 = "make a lot of money"
# p2 ="buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message =  input("enter your comment:")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this is a spam comment")
# else:

#     print("this is not a spam commnet")  

# username = input("enter username:")

# if(len(username)<10):
#     print("username is valid")
# else:
#     print("not valid")

#multipication of a number using for loop
# n = int(input("enter a number: "))
# for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")

#create all person name stored in list with letter s

# l = ["aditi","sneha","sara","riya","simran"]
# for name in l:
#     if(name.startswith("s") ):
#       print(name)

#multipication of a number using while loop
# n = int(input("enter a number: "))
# i = 1
# while(i<=10):
#     print(f"{n} X {i} = {n*i}")
#     i+=1

#find no. is prime or not
# n = int(input("enter a number: "))
# for i in range(2,n):
#     if(n%i==0):
#         print("not prime")
#         break
# else:
#     print("prime")

# n = int(input("enter a number: "))
# i = 0
# sum = 0
# while(i<=n):
#     sum = sum + i
#     i+=1
# print(sum)

#factorial of no. using while loop 
# n = int(input("enter a number: "))
# product = 1
# for i in range(1,n+1):
#     product = product*i
# print(f"factorial of {n} is {product}")

# star pattern 
# n = int(input("enter no. of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
    # print()

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
    
#     for j in range(rows - i):
#         print(" ", end="")
    
#     for k in range(2 * i - 1):
#         print("*", end="")
    
#     print()

#to print multiplication table in reverse order
# n = int(input("enter a number: "))
# for i in range(10,0,-1):
#     print(f"{n} X {i} = {n*i}")


#function and recursion pracice 
#1. wap using funtions find the greatest of 4 numbers
# def greatest(a,b,c,d):
#     if(a>b and a>c and a>d):
#         return a
#     elif(b>a and b>c and b>d):
#         return b
#     elif(c>a and c>b and c>d):
#         return c
#     else:
#         return d
    
# a= 1    
# b= 2
# c= 3
# d= 4
# print(greatest(a,b,c,d))

#wap to concert celcuis to fahrenheit using functions
# def cel_to_fah(c):
#     f = (c*9/5)+32
#     return f
# c = int(input("enter temperature in celcius: "))
# print(f"temperature in fahrenheit is: {cel_to_fah(c)}")

#wap sum off first n natural no. using recursion
# def sum(n):
#     if(n==1):
#         return 1
#     else:
#         return n + sum(n-1)
# n = int(input("enter a number: "))
# print(sum(n))

#wap print a pattern of first n li nes for n = 3
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(5)

# def inches_to_cm(inches):
#     cm = inches * 2.54
#     return cm
# n = int(input("enter length in inches: "))
# print(f"length in cm is: {inches_to_cm(n)}"

#print multiplication table of given number
# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# n = int(input("enter a number: "))
# table(n)
#wap to read text from given file poem.txt and find out it contain word twinkle
# f = open("myfile.txt")
# c=f.read()
# if("twinkle" in c):
#     print("twinkle i spresent")
# else:
#     print("not present")
# f.close()

#write a program to gerate multiplication table  from 2 to 20 and write in differet fles

# def generateTable(n):
#     with open(f"table_of_{n}.txt", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{n} X {j} = {n*j}\n")

# # Generate tables from 2 to 20
# for i in range(2, 21):
#     generateTable(i)

#MODULES EXAMPLES


#
# import custom
# print("reversed string is:", custom.reverse_str())

# print(custom.square(5))
# print(custom.cube(3))


# c = float(input("Enter temperature in Celsius: "))
# print("Fahrenheit =", custom.celsius_to_fahrenheit(c))

# f = float(input("Enter temperature in Fahrenheit: "))
# print("Celsius =", custom.fahrenheit_to_celsius(f))

# print("area of circle:",custom.area_of_circle(5))
# print("area of rectangle:",custom.area_of_rectangle(4, 6))
# print("area of triangle:",custom.area_of_triangle(3, 8))

# print("hello ! have a great day ",custom.say_hello)


# A = [1, 2, 2, 3, 4, 4, 5,]

# result = custom.unique_list(A)
# print("Unique elements:", result)
print("hello")