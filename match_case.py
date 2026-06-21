#Match Case Statement: 

'''The match-case statement is used to compare a value
with multiple cases and execute the matching block of code.
It provides a cleaner and more readable alternative to
multiple if-elif-else statements.'''

x = int(input("Enter the value of x(1-5): "))
#x is the variable to match 

match  x:
    #if x is 0 
    case 0:
        print("x is Zero")
    case 1:
        print("x is One")
    case 2: 
        print("x is Two")
    case 3: 
        print("x is Three")
    case 4: 
        print("x is Four")
    case 5: 
        print("x is Five")
    case _:
        print("Invalid number")
print()

#Practice Question:
#Write a Python program that takes a day number (1-7) as input
#and displays the corresponding day name using a match-case statement.
#
#1 -> Sunday
#2 -> Monday
#3 -> Tuesday
#4 -> Wednesday
#5 -> Thursday
#6 -> Friday
#7 -> Saturday
#
#If the user enters any other number, print "Invalid Day".
print("Practice-")
day = int(input("Enter day  number(1-7): "))

match day: 
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3: 
        print("Tuesday")
    case 4: 
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7: 
        print("Saturday")
    case _:
        print("Invalid Day")
print()

#Using if-else conditions 
print("Using if-else statement")
a = int(input("Enter a number: "))

match a:
    case _ if a < 0:
        print("Negative Number")
    case _ if a == 0:
        print("Zero")
    case _:
        print("Positive Number")


#Match-case makes the code more readable when dealing with multiple fixed values.
#case _ represents the default case (similar to default in C/Java).