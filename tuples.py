#Tuples in python 
#Definition : A tuple is a built in data type that stores multiple values likea list, but it is immutable(cannot be changed after creation)

tup = (23,44,36,86,43)
print(tup)   #all tuple
print(tup[0]) #23
print(tup[0:5])   #All tuple
print(type(tup))

#Empty tuples 

emptytuple = ()
print(type(emptytuple))

singletuple = (1,)
print(singletuple)
print(tup.index(44))
print(tup.count(23))
print(tup.count(4))