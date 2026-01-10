#Creating a set
names = {"Sia", "Mia", "Tia"}

#Printing a set
print(names) #Output: {'Mia', 'Tia', 'Sia'}

#Checking the type of set
print(type(names)) #Output: <class 'set'>

#Length of the set
print(len(names)) #Output: 3

#Accessing items of a set
for name in names:
    print(name)

'''Output:
Sia
Tia
Mia
'''

#Checking if an item is present in the set
if "Mia" in names:
    print("Mia is present in the set.")

#Checking if an item is not present in the set
if "Ria" not in names:
    print("Ria is not present in the set.")

#Adding elements to a set
names.add("Lia")
print(names) #Output: {'Mia', 'Tia', 'Lia', 'Sia'}

names.add("Sia") #Adding duplicate element
print(names) #Output: {'Mia', 'Tia', 'Lia', 'Sia'}

#Adding another sequence to a set
more_names = ["Ria", "Nia"]
names.update(more_names)
print(names) #Output: {'Mia', 'Tia', 'Lia', 'Ria', 'Nia', 'Sia'}

#Removing elements from a set
names.remove("Nia")
print(names) #Output: {'Mia', 'Tia', 'Lia', 'Ria', 'Sia'}

names.discard("Pia")
print(names) #Output: {'Mia', 'Tia', 'Lia', 'Sia', 'Ria'}

#Joining 2 sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'f'}
s3 = s1.union(s2)
print(s3) #Output: {'d', 'a', 'f', 'c', 'e', 'b'}

s1.update(s2) #Merging s2 into s1
print(s1) #Output: {'d', 'a', 'f', 'c', 'e', 'b'}

s3.intersection_update({'a', 'b', 'x'}) #Keeping only duplicates while joining
print(s3) #Output: {'a', 'b'}

s3.symmetric_difference_update({'b', 'c', 'y'}) #Keeping all values except duplicates
print(s3) #Output: {'a', 'c', 'y'}