#Lists in python
#Definition : A list is a built in data type that can store multiple values in a single variable.
#List are mutable(Can be changed) and can store different data types.
#Example : Marks = [87,90,67,89,68]
          #foods = ["samosa","galebi","burger"]
          #student = ["Anshul vishwakarma", 21, "Bhopal"]
#Accessing elements (Indexing ): 
#Each item in a list hass an index starting from 0.
#foods = ["samosa","galebi","burger"]
       #     0        1        2

foods = ["samosa","galebi","burger"]
print(foods[0])
print(foods[1])
print(foods[2])
student = ["Anshul vishwakarma", 21, "Bhopal"]
print(student[1])
print(student[0:3])

#Modify Elements: 
#Lists are changeable.
foods[0] = "anshul"
print(foods)

#List Slicing: You can extract parts of a list using slicing.

marks  = [433, 45,5,78,33, 37]
print(marks[0:6])
print(marks[:7])
print(marks[4:])
print(marks[:])

#List Functions 
'''
      Function                Description                     Example
len(list)              Returns length of list            len(marks) -> 6
max(list)              Returns largest value             max(marks) -> 433
min(list)              Returns smallest value            min(marks) -> 5'''

print(len(marks))
print(max(marks))   #agar aapki list me ek hi  data type akela hoga tab hi max() and min() functions kaam karenge
print(min(marks))

#common List method
'''
   Method               Description                             Example
.append(el)         Adds element at the end                 marks.append(54)
.insert(i,el)       Inserts element at index                marks.insert(4,32)
.remove(el)         Removes first occurrence                marks.remove(5)
.pop(i)             Removes element at index                marks.pop(433)
.sort()             Sorts list in ascending order           marks.sort()
.reverse()          Reverse the list                        marks.reverse()'''

marks  = [433, 45,5,78,33, 37]
print(marks)
marks.append(54)
print(marks)
marks.insert(3,99)
print(marks)
marks.remove(5)
print(marks)
marks.pop(4)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
