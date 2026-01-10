def add(a, b=0):
    print("a:", a)
    print("b:", b)
    return a + b

#Positional Arguments
print(add(1, 2)) #1 and 2 are positional arguments

'''Output:
a: 1
b: 2
3
'''

#Keyword/Named Arguments
print(add(a=1, b=2)) #a and b are keyword arguments
#OR
print(add(b=2, a=1)) #Sequence doesn't matter

'''Output:
a: 1
b: 2
3
'''

#Default Arguments
print(add(3)) #b is default to 0

'''Output:
a: 3
b: 0
3
'''

#Arbitrary Arguments - *args
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(addAllNumbers(1, 2, 3, 4, 5)) #1, 2, 3, 4, 5 are arbitrary arguments

#Output: 15

#Arbitrary Arguments - **kwargs
def studentInfo(**kwargs):
    for x, y in kwargs.items():
        print(x, "is", y)

studentInfo(name="John", age=25, city="New York") #name, age, city are keyword arguments