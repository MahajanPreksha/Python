#String
name = "Preksha"

#Integer
age = 21

#Floating number
percentage = 90.6

#Boolean
is_student = True

print(name, age, percentage, is_student) #Output: Preksha 21 90.6 True

#Updating value of percentage
percentage = 94.0
print(percentage) #Output: 94

#Type of variable
print(type(name)) #Output: <class 'str'>

print(type(age)) #Output: <class 'int'>

print(type(percentage)) #Output: <class 'float'>

print(type(is_student)) #Output: <class 'bool'>

#Contatenation of strings
print("My name is " + name + ".") #Output: My name is Preksha.
#OR
print("My name is " + name + " and I am", age, "years old.") #Output: My name is Preksha and I am 21 years old.

#Print expressions
print("My percentage has changed to", percentage-1, ".") #Output: My percentage has changed to 93.0 .

#Print with separator
print(name, age, percentage, is_student, sep="-") #Output: Preksha-21-94.0-True

x = 1
y = 2
z = 3
print(x, y, z, sep="->") #Output: 1->2->3