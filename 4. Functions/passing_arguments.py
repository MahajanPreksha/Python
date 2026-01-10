#Pass by Value
def addOne(x):
    x = x + 1
    print("Inside function:", x)

x = 5
addOne(x)
print("Outside function:", x)

'''Output:
Inside function: 6
Outside function: 5
'''

#Pass by Reference
def modifyList(lst):
    lst.append(4)
    #lst = [4, 5, 6] --> This will not modify the original list because it creates a new list
    print("Inside function:", lst)

lst = [1, 2, 3]
modifyList(lst)
print("Outside function:", lst)

'''Output:
Inside function: [1, 2, 3, 4]
Outside function: [1, 2, 3, 4]
'''