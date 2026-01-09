#Arithmetic Operators
print("Sum:", 4 + 3)
print("Difference:", 4 - 3)
print("Product:", 4 * 3)
print("Division:", 4 / 3)
print("Floor Division:", 4 // 3)
print("Remainder:", 4 % 3)
print("Exponentiation:", 4 ** 3)

'''Output:
Sum: 7
Difference: 1
Product: 12
Division: 1.3333333333333333
Floor Division: 1
Remainder: 1
Exponentiation: 64
'''

#Assignment Operators
n1 = 5
n2 = n1
print(n1, n2) #Output: 5 5

n2 *= n1
print(n1, n2) #Output: 5 25

#Comparison Operators
print(4 == 3)
print(4 != 3)
print(4 > 3)
print(4 < 3)
print(4 >= 3)
print(4 <= 3) 

'''Output:
False
True
True
False
True
False
'''

#Logical Operators
exp1 = 2 > 1
exp2 = 5 < 4

print("exp1 and exp2:", exp1 and exp2)
print("exp1 or exp2:", exp1 or exp2)
print("not exp1:", not exp1)

'''Output:
exp1 and exp2: False
exp1 or exp2: True
not exp1: False
'''

#Identity Operators
x = 5
y = 5
print("If x is y", x is y)
print("If x is not y", x is not y)

'''Output:
If x is y True
If x is not y False
'''

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("if banana is present in fruits:", "banana" in fruits)
print("if mango is not present in fruits:", "mango" not in fruits)

'''Output:
if banana is present in fruits: True
if mango is not present in fruits: True
'''

#Bitwise Operators
a = 5
b = 3
print("a and b:", a & b)
print("a or b:", a | b)
print("a xor b:", a ^ b)

'''Output:
a and b: 1
a or b: 7
a xor b: 6
'''