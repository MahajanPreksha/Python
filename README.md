# Introduction to Programming
Programming is creating a set of instructions i.e. a program that tells a computer how to perform a task.

Types of Languages:
1. Low Level Language/Machine Code: It is the language/code that a machine understands. It is in the form of 0s and 1s.
2. High Level Language/Source Code: It is the language that humans understand. It can be: C/C++, Python, Java, etc.

To convert Source Code to Machine Code, a compiler is used.

But in case of Python, following process occurs:

Source Code ---> Compiler ---> Byte Code ---> Interpreter ---> Machine Code

# Introduction to Python ([Python Essentials](1.%20Python%20Essentials))
Python is one of the most famous programming languages.

It is easy to read, write and understand any Python code. So, it is a beginner-friendly programming language.

Python codes are quite concise.

It is an Open Source programming language.

It has a support of a very large community.

It is also a very versatile language as it is used in:
- Web Development
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Data Analytics
- Internet of Things (IOT)

## Python Comments
Comments are used to write simple, descriptive sentences to make the code easier to understand.

Single-line comments begin with # while multi-line comments begin and end with """.

```python
#This is a single-line comment.
''' This is
a multi-line
comment. '''
```

## Indentation in Python
It is the number of spaces provided before write a particular line in the code.

Indentation matters in Python.

## Python CLI
CLI stands for Command Line Interface.

Upon writing Python3 in CLI, it launches REPL (Read Evaluate Print Loop).

To exit the REPL environment, press Ctrl+D or write `exit()`.

## Variables and their Declarations
Variables are containers (memory spaces in computers) that are used to store data which can be of different types.

```python
x = 5 #Data Type: Integer
y = 5.2 #Data Type: Float
z = "John" #Data Type: String
a = False #Data Type: Boolean
b = None #Data Type: Null
```

In Python unlike other programming languages, variables need not be declared with any particular type. Thus, Python is a **dynamically-typed** programming language.

> Variables should be given a meaningful name.

### Naming Rules for Variables
1. A variable name must start with a letter or the underscore character.
> `name` and `_name` are valid variable names.
2. A variable name cannot start with a number.
> `4students` is an invalid variable name.
3. A variable name can only contain alphanumeric characters and underscores (A-Z, a-z, 0-9, _).
> `*name` is an invalid variable name.
4. Variable names are case-sensitive.
> `count`, `Count` and `COUNT` are three different variables.
5. A variable name cannot be any of the Python keywords.

#### Python Keywords
| False | None | True | and | as |
| ----- | ----- | ----- | ----- | -----|
| assert | break | class | continue | def |
| del | elif | else | except | finally |
| for | from | global | if | import |
| in | is | lambda | nonlocal | not |
| or | pass | raise | return | try |
| while | with | yield | | |

#### Concatenation in Strings
- Strings can be contatenated using `+` operator.
- Strings can be concatenated with different data types using `,` operator.

## Python Data Types
1. Numeric Data Type
- Int: 100, -5, 256 (Whole Numbers)
- Float: 2.5, -1.8 (Decimal Numbers)
- Complex Numbers: 1+2i, 60+250i (Numbers with real and imaginary parts)

2. Text Data Type
- String: It is a sequence of characters enclosed with ' ' or " ".

Example: "Preksha"

3. Boolean Data Type
- It consists of 2 boolean values: True or False.

4. Sequence Data Type
- List: It is used to store a sequence of items enclosed within [] and separated by commas.

Example: [1, 2, 3, 4, 5]
- Tuple: It is used to store a sequence of unmodifiable items of  enclosed within () and separated by commas.

It can contain duplicate values.

Example: (1, 2, 2, 3, 3)

5. Dictionary Data Type
Data is stored in the form of key-value pairs.

Value is identified using its key which is unique.

Example: student = {"name": "Preksha", "age": 21}

6. Set Data Type
It is an unordered collection of unique items.

Example: fruits = {"apple", "banana", "cherry"}

7. None Data Type
It represents Null value.

#### ASCII and Unicode Values:
ASCII stands for American Standard Code for Information Interchange.

It helps to represent characters as numeric codes.

Examples:
- A-Z = 65-90
- a-z = 97-122
- 0-9 (as characters) = 48-57
- space (" ") = 32

Inbuilt function to know the ASCII value is: `ord()`.

Inbuilt function to know the character from the ASCII value is: `chr()`. (Returns as string)

## Taking Input
Input can be taken using `input()`.

```python
name = input("Enter your name: ")
```

Input is always captured as string. To input other data types, we use the process of type-casting.

> Type-casting: It is the process of converting one data type to another.

```python
age = int(input("Enter your age: "))
```

## Operators and its Types
Operators are used to perform some sort of computations using operands.

1. Arithmetic Operators: They are used for arithmetic operations.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| + | Addition | n1 + n2 | Adds n1 and n2 |
| - | Subtraction | n1 - n2 | Subtracts n2 from n1 |
| * | Multiplication | n1 * n2 | Multiplies n1 and n2 |
| / | Division | n1 / n2 | Divides n1 by n2 (returns a floating point number) |
| % | Modulus | n1 % n2 | Returns remainder upon dividing n1 by n2 |
| ** | Exponentiation | n1 ** n2 | Raises n1 to the power of n2 |
| // | Floor division | n1 // n2 | Returns nearest whole number upon dividing n1 by n2 |

2. Assignment Operators: They are used for assignment operations.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| = | Assignment | n1 = n2 | Assigns value to a variable |
| += | Addition Assignment | n1 += n2 | Same as n1 = n1 + n2 |
| -= | Subtraction Assignment | n1 -= n2 | Same as n1 = n1 - n2 |
| *= | Multiplication Assignment | n1 *= n2 | Same as n1 = n1 * n2 |
| /= | Division Assignment | x /= n2 | Same as n1 = n1 / n2 |
| %= | Modulus Assignment | n1 %= n2 | Same as n1 = n1 % n2 |
| //= | Floor Division Assignment | n1 //= n2 | Same as n1 = n1 // n2 |
| **= | Exponentiation Assignment | n1 **= n2 | Same as n1 = n1 ** n2 |
| &= | Bitwise AND Assignment | n1 &= n2 | Same as n1 = n1 & n2 |
| \|= | Bitwise OR Assignment | n1 \|= n2 | Same as n1 = n1 \| n2 |
| ^= | Bitwise XOR Assignment | n1 ^= n2 | Same as n1 = n1 ^ n2 |
| >>= | Right Shift Assignment | n1 >>= n2 | Same as n1 = n1 >> n2 |
| <<= | Left Shift Assignment | n1 <<= n2 | Same as n1 = n1 << n2 |


3. Comparison Operators: They are used to compare two values.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| == | Equal to | n1 == n2 | Returns True if n1 is equal |
| != | Not Equal to | n1 != n2 | Returns True if n1 is not equal |
| > | Greater than | n1 > n2 | Returns True if n1 is greater
| < | Less than | n1 < n2 | Returns True if n1 is smaller |
| >= | Greater than or Equal to | n1 >= n2 | Returns True if n |
| <= | Less than or Equal to | n1 <= n2 | Returns True if n1 is smaller or equal |

4. Logical Operators: They work with boolean values.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| and | Logical AND | n1 and n2 | Returns True if both statements are True |
| or | Logical OR | n1 or n2 | Returns True if one of the statements is True |
| not | Logical NOT | not n1 | Reverses the result, returns False is the result is True |

5. Identity Operators: They check the identity of the variables.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| is | Identity | n1 is n2 | Returns True if both variables are the same object |
| is not | Not Identity | n1 is not n2 | Returns True if both variables are not the same object |

6. Membership Operators: They are used to check if a value is a member of a particular sequence.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| in | Membership | item in sequence | Returns True if a sequence with the specified value is present in the object |
| not in | Not Membership | item not in sequence | Returns True if a sequence with the specified value is not present in the object |

7. Bitwise Operators: They work with bits.

| Operator | Name | Example | Operation |
| ----- | ----- | ----- | ----- |
| & | Bitwise AND | n1 & n2 | Sets each bit to 1 |
| \| | Bitwise OR | n1 \| n2 | Sets each bit to 1 if one of the bits is 1 |
| ^ | Bitwise XOR | n1 ^ n2 | Sets each bit to 1 |
| ~ | Bitwise NOT | ~n1 | Inverts all the bits |
| << | Zero Fill Left Shift | n1 << n2 | Shifts the bits of n1 |
| >> | Zero Fill Right Shift | n1 >> n2 | Shifts the bits of n1 |

### Operators Precedence
It is a set of rules that determines the hierarchy of operators in an expression with multiple operators.

| Precedence Level | Operators |
| ----- | ----- |
| 1 | () |
| 2 | ** |
| 3 | /, %, // |
| 4 | * |
| 5 | +, - |
| 6 | >>, <<>> |
| 7 | &, /|, ^ |
| 8 | ==, !=, >, <, >=, <= |
| 9 | not, and, or |

## Inbuilt Functions
Inbuilt functions are the functions that are already defined in Python.

1. type(): It is used to find the datatype of a variable.

2. int(): It is used to convert a datatype into an integer.

3. float(): It is used to convert a datatype into a floating number.

4. str(): It is used to convert a datatype into a string.
---

# Control Statements ([Conditionals and Loops](2.%20Conditionals%20and%20Loops/))
Control statements allow the programmer to control the flow of the program.

## Conditionals
Conditionals are used to perform different actions based on different conditions.

1. if-else statement
2. nested
3. if-else ladder
4. ternary operator
5. match

> For multiple conditions, use logical operators 'and' and 'or' with if-elif-else statements.

## Loops
Loops are used to execute a block of code repeatedly until a certain condition is met.

1. For Loop
2. While Loop
---

# Python Collections ([3. Python Collections](3.%20Python%20Collections/))
Collections in Python are used to store sequence/collection of items in one variable.

Examples:
1. List
2. Tuple
3. Dictionary
4. Set

## List
It allows us to store multiple items in a single variable using square brackets.

Example:
```python
fruits = ["apple", "mango", "cherry"]
```

Items of a list are:
- Indexed: Indexing starts from 0 to access any item of the list.
- Ordered: Items are present in the same way as they had been put into the list.
- Mutable: Items can be updated/modified using indexes.
- Duplicates allowed: Any item can appear multiple times.
- Any data type: Different lists can store items of any data type.
- Mix of different data types: Items of a list can be heterogenous too.

### Accessing items of a List
- Indexing: Lists have 0-based indexing.
- Negative Indexing: Negative indexing begins from -1 in the list.
- Range of indices: It is used to access a sublist between starting index (inclusive) and ending index (exclusive).
- Range of negative indices: It is used to access a sublist between starting index (inclusive) and ending index (exclusive) but with negative indices.

### Adding elements to a List
1. append(): It adds an item to the end of the list.
2. insert(): It adds an item at the specified index.
3. extend(): It adds multiple items to the end of the list.

### Removing elements from a List
1. remove(): It removes the first occurrence of the specified item.
2. pop(): It removes the item at the specified index. If index is not provided, then the last item will be removed.

### Changing items in a List
1. At an index
2. In a range

### Sorting a List
Sorting is used to arrange the items of a list in a specific order.

There are two ways to sort using ```sort()``` method:

1. Ascending (By default)
2. Descending

### List Comprehension
It is used to create a new list from an existing list.

## Tuple
It allows us to store multiple items in a single variable using round brackets.

```python
colours = ("red", "green", "blue")
```

Items of a tuple are:
- Ordered: Items are present in the same way as they had been put into the tuple.
- Immutable: Items cannot be modified.
- Duplicates allowed: Any item can appear multiple times.
- Any datatype: Different tuples can store items of any data type.
- Mix of different datatypes: Items of a tuple can be heterogenous too.

### Accessing items of a Tuple
- Indexing: Tuples have 0-based indexing.
- Negative Indexing: Negative indexing begins from -1 in the tuple.
- Range of indices: It is used to access a sub-tuple between starting index (inclusive) and ending index (exclusive).
- Range of negative indices: It is used to access a sub-tuple between starting index (inclusive) and ending index (exclusive) but with negative indices.

### Tuples v/s Lists
| Property | Tuple | List |
| ----- | ----- | ----- |
| Syntax | Enclosed within () | Enclosed within [] |
| Mutability | Immutable | Mutable |
| Iteration | Faster | Slower |

> Note: Tuples that contain immutable elements can be used as a key for dictionary.

### Reversing a Tuple
To iterate through a tuple in a reversed order, we use ```reversed()``` method.

## Set
It allows us to store multiple items in a single variable using curly braces.

```python
fruits = {"apple", "banana", "cherry"}
```

Items of a set are:
- Unordered: Items are not in any particular order.
- Immutatable: Items cannot be modified.
- Unindexed: Indexing doesn't exist for sets.
- Duplicates not allowed: Any item can appear only once.
- Any datatype: Different sets can store items of any data type.
- Mix of different datatypes: Items of a set can be heterogenous too.

### Adding elements to a Set
1. add(): It is used to add an element to the set.
2. update(): It is used to add another sequence to the set.

### Removing elements from a Set
1. remove(): It removes the specified item from the set. If item is not found, it will throw a KeyError.
2. discard(): It removes the specified item from the set. If item is not found, it will not throw an error.

## Dictionary
It allows us to store multiple items in a single variable using curly braces in the form of key-value pairs.

```python
numbers = {'John': 1111, 'Ria': 2222, 'Joy': 3333}
```

Items of a dictionary are:
- Ordered: Items are present in the same way as they had been put into the dictionary.
- Unindexed: Elements cannot be accessed using indices.
- Changeable: Key-value pairs can be changed.
- Duplicates not allowed: Keys have to be unique while values need not to be.
- Any datatype: A key can store values of any data type.

### Accessing items of a Dictionary
1. Using keys
2. Using get() method
3. Using keys() method

### Adding elements to a Dictionary
1. Using new key
2. Using update() method

### Removing elements from a Dictionary
1. pop(): It removes the item with the specified key name.
2. popitem(): It removes the last inserted key-value pair.
3. clear(): It will remove all items from te=he dictionary.
---

# Functions ([4. Functions](4.%20Functions/))
Functions are blocks of code that perform a specific task.

> Input ---> Function ---> Output

## Types of Functions
1. Built-in Function: A function whose code is already available and can be directly used is called a built-in function.

Example: print(), input(), etc.

2. User-defined Function: A function created by a user is called user-defined function.

## Creating a Function
Syntax:
```python
def function_name(parameters):
    #statement
    return expression
```

- def: It is a keyword that is used to define a function.
- function_name: It is the name of the user-defined functions.
- parameters: These tell us what input the function is expecting
- Inside the function, there would be the body of statement
- return: This statement will give output.

## Calling a function
Syntax:
```python
function_name(arguments)
```
- arguments: Arguments are the values which we pass as input to a function

### Types of Arguments
1. Positional Arguments
2. Keyword/Named Arguments
3. Default Arguments
4. Arbitrary Arguments (variable-length arguments *args and **kwargs)
- *args are stored in a tuple.
- **kwargs(keyworded arguments/key-value pairs arguments) are stored in dictionary.

## Pass by Value and Pass by Reference
1. Pass by Value: When immutable objects like: strings, integers, floating point numbers and tuples are passed to a function, a copy of the object is created.

If any change is made to them inside function, it doesn't affect the original variable outside function.

2. Pass by Reference: When mutable objects like: list and dictionaries are passed to a function, a reference to the actual object is passed to the function.

Changes inside the function will affect the original object.

---

# Recursion ([5. Recursion](5.%20Recursion/))
When a function calls itself to solve a problem which is divided further into sub-problems, it is called as recursion.

Syntax:
```python
#Function Definition
def recurse():
    recurse() #Recursive Call

recurse() #Function Call
```

## Base Case and Recursive Case
There are 2 parts of a recursive function:
1. Base Case: It is the stopping point of the recursion.
2. Recursive Case: It is the part where a function calls itself for solving a subproblem.

## Call Stack and Recursive Calls
In memory, recursion works with the help of call stack.

For every recursive call, a stack frame gets added to the call stack and this keeps on going till you reach the base case.

---

# Strings ([6. Strings](6.%20Strings/))
Strings are a sequence of characters enclosed within single, double or triple quotes.

They are immutable i.e. contents of a string can't be modified. Instead, new strings can be created by manipulating the original string.

> Multiline strings can be assigned to a variable using triple quotes.

Strings have array-like indexing which begins from 0 and negative indexing starts from -1.

## Escape Characters
These are special characters that are used to represent some non-printable/reserved characters in strings.

| Code | Result |
| ---- | ---- |
| \' | Single Quote |
| \\ | Backslash
| \n | New Line |
| \r | Carriage Return |
| \t | Tab |
| \b | Backspace |
| \f | Form Feed |
| \ooo | Octal Value |
| \xhh | Hex Value |
---

# Object Oriented Programming (OOP) ([7. Object Oriented Programming](7.%20Object%20Oriented%20Programming/))
It is a programming paradigm where the software design resolves around objects and data over functions, unlike Procedure Oriented Programming.

### Use of OOPs in Python
OOPs is used in Python because:
1. It helps to mimic the real-world entities and their interactions.
2. It helps in code resuability.
3. It also helps in organisation and maintainability of the code.

## Classes and Objects
**Classes**: Classes are user-defined data types. They are like a bluprint/template for an object.

**Objects**: An object is an instance of type 'class'. They mimic real-world entities.

Example: A class 'Car' with properties/attributes like: length, colour and methods/functions like: get_fuel(), etc.

Objects of the class 'Car' can be Audi, Nissan, Volvo, etc. They all have the attributes and methods of the class.

Syntax to create a class and an object:
```python
class ClassName:
    #Attributes and Methods
    pass

object1 = ClassName()
```

To access an attribute or a function of a class by the object, dot (.) operator is used.

## Class Constructor
A constructor is a special function that gets invoked everytime an object is created for that class.

Syntax:
```python
class ClassName:
    def __init__(self, param1, param2, ...):
        #Initialise instance variables/attributes here
```

## Attributes
Attributes can be of two types:
1. Class Attributes: These are defined inside the class and all the object instances have these attributes.
2. Instance Attributes: These are specific to a particular instance/object.

## Access Modifiers
Access modifiers are used to control the visibility/access of class attributes and functions.

There are 3 types of access modifiers:
1. Public: Attributes and functions of a class can be accessed outside the class too.
2. Private: Attributes and functions of a class can be accessed inside the class only.
3. Protected: Attributes and functions of a class can be accessed outside the class and they should be accessed only inside the class or via a sub-class.

> By default, attributes and functions are **public**.

## Properties of OOP
There are 4 properties/pillars of OOP:
1. Inheritance
2. Polymorphism
3. Abstraction
4. Encapsulation 

### Inheritance
It is a property of OOP where one class can inherit properties (attributes and functions) from another class.

Syntax:
```python
class SuperClass:
    #Attributes and Methods of SuperClass go here.

class SubClass(SuperClass):
    #Additional Attributes and Methods of SuperClass go here.
```

#### Types of Inheritance
There are 5 types of inheritance:
1. Single Inheritance: One child class inherits from one parent class.

A ---> B where A is the parent class and B is the child class.

2. Multiple Inheritance: One child class inherits from multiple parent classes.

A ---> C <--- B where A, B are parent classes and C is the child class.

3. Multilevel Inheritance: A child class inherits from parent class which inherits from grandparent class.

A ---> B ---> C where A is the base/grandparent class, B is the intermediary/parent class and C is the derived/child class.

> There are 2 or more levels of inheritance.

4. Hierarchical Inheritance: Muliple child classes inherit from one parent class.

B <--- A ---> C where A is the parent class and B, C are child classes.

5. Hybrid Inheritance: It is a mix of multilevel and hierarchical inheritance.

A <--- C ---> B and C ---> D where A, B are parent classes of C, C is a child class of A and B and D is the child class of C.

### Polymorphism
It is made up of two words: Poly meaning many and Morphism meaning forms.

It allows objects of different classes to behave as objects of the same super class.

#### Types of Polymorphism
There are 2 types of polymorphism:
1. Compile-Time Polymorphism: It is resolved during compile-time.

It is achieved through:
- Method Overloading: Multiple methods with same name but different paramters
- Operator Overloading: Giving special meaning and functioning to different mathematical operators

2. Run-Time Polymorphism: It is resolved during run-time.

It is achieved through Method Overriding.

### Abstraction
It allows us to focus on 'what' of the object rather than 'how' of the object.

### Encapsulation
It bundles the attributes (data) and methods (functions) together in one entity which is called as class.

# Exception Handling in OOP
Sometimes, our code has some lines that can throw exceptions at run-time.

To handle it, we use three keywords:
1. try: it has the code which might throw an exception
2. except: if exception occurs, it has the code to handle the exception along with its ExceptionType (ValueError, TypeError, ZeroDivisionError, etc.)
3. finally: it has the code which will be executed regardless of the exception
---