#Create a list
fruits = ["apples", "bananas", "cherries", "mangoes"]

#Printing the list
print(fruits) #Output: ['apples', 'bananas', 'cherries']

#Checking the type of list
print(type(fruits)) #Output: <class 'list'>

#Length of the list
print(len(fruits)) #Output: 3

#Checking if an item is present in the list
if "bananas" in fruits:
    print("Bananas are a part of the list.")

#Checking if an item is not present in the list
if "grapes" not in fruits:
    print("Grapes are not a part of the list.")

#Indexing in list
print(fruits[1]) #Output: bananas

#Negative Indexing in list
print(fruits[-3]) #Output: bananas

#Accessing a sublist
print(fruits[1:3]) #Output: ['bananas', 'cherries']
print(fruits[-3:-1]) #Output: ['bananas', 'cherries']

#Inserting elements to a list
fruits.append("kiwis")
print(fruits) #Output: ['apples', 'bananas', 'cherries', 'mangoes', 'kiwis']

fruits.insert(2, "oranges")
print(fruits) #Output: ['apples', 'bananas', 'oranges', 'cherries', 'mangoes', 'kiwis']

more_fruits = ["grapes", "pineapples"]
fruits.extend(more_fruits)
print(fruits) #Output: ['apples', 'bananas', 'oranges', 'cherries', 'mangoes', 'kiwis', 'grapes', 'pineapples']

#Removing elements from a list
fruits.remove("bananas")
print(fruits) #Output: ['apples', 'oranges', 'cherries', 'mangoes', 'kiwis', 'grapes', 'pineapples']

fruits.pop(1)
print(fruits) #Output: ['apples', 'cherries', 'mangoes', 'kiwis', 'grapes', 'pineapples']

fruits.pop()
print(fruits) #Output: ['apples', 'cherries', 'mangoes', 'kiwis', 'grapes']

#Changing items in a list
fruits[2] = "watermelons"
print(fruits) #Output: ['apples', 'cherries', 'watermelons', 'kiwis', 'grapes']

fruits[1:3] = ["peaches", "plums"]
print(fruits) #Output: ['apples', 'peaches', 'plums', 'kiwis', 'grapes']

fruits[1:3] = "papayas"
print(fruits) #Output: ['apples', 'p', 'a', 'p', 'a', 'y', 'a', 's', 'kiwis', 'grapes']

#Sorting a list
fruits.sort()
print(fruits) #Output: ['a', 'a', 'a', 'apples', 'grapes', 'kiwis', 'p', 'p', 's', 'y']

fruits.sort(reverse=True)
print(fruits) #Output: ['y', 's', 'p', 'p', 'kiwis', 'grapes', 'apples', 'a', 'a', 'a']

#List Comprehension
li = [10, 20, 30, 40, 50]

new_li = [i for i in li if i > 25]
print(new_li) #Output: [30, 40, 50]

#Copying a list
copied_fruits = fruits.copy()
print(copied_fruits) #Output: ['y', 's', 'p', 'p', 'kiwis', 'grapes', 'apples', 'a', 'a', 'a']

#Concatenating 2 lists
li2 = [60, 70, 80]

li2 = li + li2
print(li2) #Output: [10, 20, 30, 40, 50, 60, 70, 80]

#Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list) #Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[1]) #Output: [4, 5, 6]
print(nested_list[0][2]) #Output: 3