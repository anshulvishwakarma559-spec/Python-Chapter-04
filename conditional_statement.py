#Conditional Statement

'''Conditional statements allow your program to make
 decisions - run different parts of code based on certain conditions.'''

#What are conditions? 

'''A Conditions is simply a statement that can be either True or False. '''

#Example: 
age1 = 18 
print(age1>=18) # True 

#if - statement: Used to run a block of code only when the conditions True.
print("="*40)
print("if statement-")
age = int(input("Enter your age : "))
print("Your age is:",age)

if age >= 18: 
    print("Very good you are eligible to vote")
#If the condition if false, nothing happens.
print("Program complete!")


#if-else statement : 
print("="*40)
print("if-else statement-")
marks = int(input("Enter your marks : "))
print("Your marks is: ",marks)
if marks >= 33:
    print("Good, you pass")
else:
    print("Bad, you failed")

#if-elif-else statement : 
print("="*40)
print("if-elif-else statement-")
marks1 = int(input("Enter your marks1: "))
print("Your marks1 is: ",marks1)
if marks1 >= 75:
    print("Excellent!")
elif marks1 >= 33:
    print("Good, you passed!")
else:
    print("Sorry, You failed!")
print("Okay!")

#Practice Question : Write a python program that takes a number as input and prints: 
   #"Positive" if number > 0
   #"zero" if number == 0
   #"Negative" if number < 0

print("="*40)
print("Practice!")
a = int(input("Enter the value: "))
if a > 0:
    print("Positive!")
elif a == 0: 
    print("Zero!")
else:
    print("Negative!")
print("Program completed!")

#Practice -
print("="*40)
print("Apple example")
apple_price = int(input("Enter applePrice:"))
budget = int(input("Enter your budget:"))
if apple_price <= budget :
    print("Khushi, add 1 kg Apples to the card.")
else:
    print("Khushi, do not add Apples to the card.")

#Practice - 
print("="*40) 
num = int(input("Enter the value of num: "))

if num == 999 :
    print("Number is Special.")
elif num > 0:
    print("Number is Positive.")
elif num == 0:
    print("Number is Zero.")
else: 
    print("Number is Negative.")
print("I am happy now.")

#Nested if statements: 
print("="*40)
print("Nested if statement-")

num1 = int(input("Enter the value of num1: "))
if num1 < 0 :
    print("Number is Negative.")
elif num1 > 0 :
    if num1 <= 10 :
        print("Number is between 1-10")
    elif num1 <= 20  :
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")
