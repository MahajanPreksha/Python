#Creating a tuple
colours = ("red", "yellow", "green")

#Creating a tuple with 1 item
fruit = ("apple",)
#OR
fruit = tuple(("apple"))

#Checking the type of a tuple
print(type(colours))  #Output: <class 'tuple'>
print(type(fruit))    #Output: <class 'tuple'>

#Length of a tuple
print(len(colours)) #Output: 3

#Accessing items in a tuple
print(colours[1]) #Output: yellow
print(colours[-2]) #Output: yellow
print(colours[0:2]) #Output: ('red', 'yellow')
print(colours[-2:]) #Output: ('yellow', 'green')

#Checking if an item exists in a tuple
if "green" in colours:
    print("Green is in the tuple") #Output: Green is in the tuple

#Checking if an item does not exist in a tuple
if "blue" not in colours:
    print("Blue is not in the tuple") #Output: Blue is not in the tuple

#Traversing a tuple
for i in colours:
    print(i)

'''Output:
red
yellow
green
'''

#Concatenating 2 tuples
more_colours = ("blue", "brown")
colours = colours + more_colours
print(colours) #Output: ('red', 'yellow', 'green', 'blue', 'brown')

#Unpacking a tuple
colour1, colour2, colour3, colour4, colour5 = colours
print(colour1) #Output: red
print(colour5) #Output: brown