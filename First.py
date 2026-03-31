# print("hello world")
# '''print(7)
# print(12*8)'''#triple double quote also works 
# print("bye")
# print("hello i'm Aditi \n from Lucknow")
#print("hey i'm a good girl\n and good singer")#

#1.VARIABLES
# a=2
# b=3 
# name = "aditi"
# print(name)

#.DATA TYPES
# a = 1    #a is an integer
# b= 6.44 # b is a floating point number
# c = "aditi" #c is string
# d = False # d is boolean variable
# e = None # e is a none type variable

# 3.OPERATORS IN PYTHON

#1. Arithmatic 
# a= 32
# b= 34
# c= a+b
# print(c)

#2.ASsignment 
# a =4-2 #assingn 4-2 in a
# print(a)
# b=6
# b+=3 # increment the value of b by 3 and then assign it to b
# b-=3 # dec#ement the value of b by 3 and then assign it to b
# print(b)

#COMparison
# a = 5>=4
# a= 5!=7
# a= 5==5
# print(a)

#LOGical
# a = 1 or 5 
# a = True or False    
# TRUTH TABLE OF "OR"
#  #true or false is true
                      #true or true is true
                    #False or true is true
                    #false or false is false
#TRUTH TABLE OF "AND"
                      #true and false is false
                      #true and true is true
                    #False and true is false
                    #false and false is false
# print(not(True))

 
#TYPE
# a= "1.2 "
# b = float(a) #a but the  type should be float
# t = type(b ) #class <int>
# print(t) 

#INPUT FUNTION
# a = "31.2"
# b = float(a)# a but the type should be float
# t = type(a)
# print(t)

#3.STRINGS
# name = "aditi"
# nameshort = name[0:3]#start from index 0 all the way till 3 
# character1 = name[1]
# print(character1)
# print(name[-4:-1])
# print(name[1:4])
# print(name[:4])#same as print(name[0:4])
# print(name[1:])#same as print(name[1:5]) 

#STR.FUNCTIONS
# name = "aditi"
# print(len(name))
# print(name.endswith("iti"))
# print(name.startswith("Ad"))
# print(name.capitalize()) 

#ESCAPE SEQUENCE CHARACHTERS
# eg. \n = new line , \t = tab , \' = singlequote , \\ backslash
# a = "aditi is a good girl \t \n but not a bad girl "
# print( a)

#4. LISTS AND TUPLES

# friends = ["apple", "rohan", 7, 8.9, False]
# print(friends[0])
# friends[0] = "grapes" # unlike strings lists are mutable
# print(friends[0])
# print(friends[1:4])

# friends.append("aditi")# lists method
# print(friends)

#TUPLE
# a = (1,5,6,) # tuple cannot be changed
# print(type(a))
# print(a)
# a= (1,5,5,5,5,6,)
# b = a.count(5)
# print(b)

#5. DICTIONARIES (collection of key value pairs)
# marks = {
#     "aditi ": 100,
#     "rohan": 67 }
# print(marks,type(marks))
# print(marks["aditi "])

#dict methods
# print(marks.items())
# print(marks.keys())print(marks.values())
# marks.update({"aditi ":99 , "rishi":20})
# print(marks)
# print(marks.get("shivika"))

#SETS (collection of non repetive elements)

# s = {1,2,3,4}
#  e = set() #dont use s = {} it will create empty dict
# print(s,type(s))
# s.add(23)
# print(s,type(s))

# operations on sets
# len(s), s.remove,s.pop,s.clear

# s1 = {1,2,3,4}
# s2 = {1,6,7,8}
# print(s1.union(s2))
# print(s1.intersection(s2))


#6. CONDITIONAL STATEMENTS

# a =  int(input("enter your age: "))
# # if , elif, else ladder
# if(a>=18):
#     print("you are above the age of consent")
# elif(a<0):
#     print("you are entering an invalid age ")
# else:

#     print("you are below the age of consent")
 
      

#7. LOOPS in python
# i = 0
# while(i<=50):
#     print(i)
#     i+=1                   
# i = 0
# while(i<5):
#     print("aditi")
#     i = i+1

# for i in range(4):
#     print(i)

# l = [1,2,3,4,5]
# for i in l:
#     print(i)
# s = "aditi"
# for i in s:
#     print(i)

#BREAK AND CONTINUE STATEMENTS

# for i in range(100):
#     if(i==50):
#         break # exit the loop 
#     print(i) 

# for i in range(100):
#     if(i==50):
#        continue # skip the current iteration 
#     print(i) 
 
#pass statement
# for i in range(100):
#     pass # it is used to avoid error in empty loops

# i = 0
# while(i<45):
#     i+=1
#     print(i)


#8. FUNCTIONS and RECURSION

# a = 12
# b =14
# c = 45
# averagge = (a+b+c)/3
# print(averagge)


# def avg(): # funtion define kar rahe hain 
#     a = int(input("enter number 1: "))
#     b = int(input("enter number 2: "))
#     c = int(input("enter number 3: "))
#     average = (a+b+c)/3
#     print("Average is:", average)

# # Function ko call kar rahe hain 3 baar
# avg()
# print("thank you")
# avg()
# avg()

#eg. greet a user with good day
# def gooday():
#     print("good day ")

# gooday()


# TYPES OF FUNCTIONS
#built in functions - print(), input(), type(), int(), float(), str(), len()
#user defined functions - avg(), gooday()

#FUNCTION WITH ARGUMENTS AND PARAMETERS

# def gooday(name, ending): #name and ending are parameters
#      print("good day",name)
#      print(ending)
     

# gooday("aditi", "thanku") #aditi and thanku are arguments
# gooday("divya","thaanku")

#default parameter value 

# def gooday(name, ending="thanku"):  # ending has a default value
#     print(f"Good day {name}")
#     print(ending)

# gooday("Aditi")
# gooday("divya")


#RECURSION (function calling itself)

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n - 1)

# n = int(input("Enter a number: "))
# print(factorial(n))


#9. FILE I/o

# st = "this is my first file\n"

# f = open("myfile.txt", "w") # w is write mode
# f.write(st)

# f.close()

# f = open("myfile.txt") # r is read mode
# lines = f.readlines()
# print(lines, type(lines))
# f.close()

# line1 =f.readline()
# print(line1 , type(line1))
# f.close() 

# f = open("myfile.txt") # a is append mode
# print(f.read())
# f.close()

# #with staement
# with open("myfile.txt") as f:
#    print(f.read())#you dont need to close the file explicitly

#10. OBJECT ORIENTED PROGRAMMING

# class Student:
#     name = "aditi"

# s1 = Student()
# print(s1.name)


