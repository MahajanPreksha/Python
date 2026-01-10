#Creating strings
name = "Preksha Mahajan" #String using double quotes
age = 'Twenty One' #String using single quotes
role = '''Software Engineer Intern''' #String using triple quotes

print(name, age, role) #Output: Preksha Mahajan Twenty One Software Engineer Intern
print(type(name)) #Output: <class 'str'>
print(type(age)) #Output: <class 'str'>
print(type(role)) #Output: <class 'str'>

#Indexing in string
text = "Hello, World!"
print(text[0]) #Output: H
print(text[4]) #Output: o
print(text[-1]) #Output: !

#Traversing a string
#Using for loop
for i in name:
    print(i, end=' ') #Output: P r e k s h a   M a h a j a n 

print('\n')

#Using list comprehension
lst = [char for char in name]
for i in lst:
    print(i, end=' ') #Output: P r e k s h a   M a h a j a n

print('\n')

#Finding length of a string using len() function
print(len(name)) #Output: 15

#Finding a char/substring in a string using find() function
print(name.find('z')) #Output: -1 --> -1 indicates that char/substring is not present in the given string
print(name.find('a')) #Output: 6 --> Returns first occurrence of the char in the given string
print(name.find('Maha')) #Output: 8 --> Returns first occurrence of the substring in the given string

#Slicing a string using [start:stop:step] --> start is inclusive and stop is exclusive
str = "abcdef"
print(str[2:4]) #Output: cd
print(str[2:5]) #Output: cde

#Slicing from the start
print(str[:3]) #Output: abc

#Slicing till the end
print(str[3:]) #Output: def

#Slicing with negative indexing
print(str[-3:]) #Output: def
print(str[-3:-1]) #Output: de

#Modifying strings
#Converting characters to uppercase using upper() function
str1 = "new york"
str2 = str1.upper()
print(str2) #Output: NEW YORK

#Converting characters to lowercase using lower() function
print(str2.lower()) #Output: new york

#Capitalising the first character of string using capitalize() function
str3 = "new york"
print(str3.capitalize()) #Output: New york

#Stripping/Removing any trailing whitespaces using strip() function
str4 = "       hello      "
print(str4.strip()) #Output: hello

#Replacing a character/substring in a string using replace() function
#Syntax: string.replace(old_substring, new_substring, count) --> Replace old substring with new substring 'count' number of times and if count isn't mentioned, all instances will get replaced.
str5 = "Hello world, what a nice world it is!"
print(str5.replace("world", "earth")) #Output: Hello earth, what a nice earth it is!

#Splitting a string into a list of substrings using split() function
'''Syntax: string.split(sep, maxsplit)
By default, sep = " " and maxplit (how many times a string will be splitted at the separation) has no limit.
'''
str6 = "apple banana mango"
print(str6.split()) #Output: ["apple", "banana", "mango"]

str7 = "ria,pia,tia,sia"
print(str7.split(',')) #Output: ['ria', 'pia', 'tia', 'sia']

#Concatenation in a string
str8 = "Hello World, "
str9 = "Great place"
print(str8 + str9) #Output: Hello World, Great place

#String formatting to insert variable values in a string using format() function
studentName = "Preksha"
studentMarks = 100
str10 = "The student name is {s} and marks are {m}.".format(s=studentName, m=studentMarks)