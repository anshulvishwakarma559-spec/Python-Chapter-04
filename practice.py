#Practice Question : Write a program that takes names of 3 favorite foods from the user and stores them in a list. then print the list and its length.

food1 = input("Enter food 1 : ")
food2 = input("Enter food 2 : ")
food3 = input("Enter food 3 : ")

foodlist = [food1,food2,food3]
print("My favorite foods is: ",foodlist)
print("Length of favorite food : ",len(foodlist))
