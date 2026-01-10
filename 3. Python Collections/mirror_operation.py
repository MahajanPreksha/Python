input_string = input("Enter the string: ")
n = int(input("Enter number of characters to mirror: "))

#Creating dictionary for mirror operations
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reverse_alphabets))

#Finding the part of the string to mirror
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#Finding the mirrored string
mirror = ""
for i in range(0, len(suffix)):
    mirror += dict1[suffix[i]]

#Creating the final string
res = prefix + mirror
print("The result is:", res)

'''Output:
Enter the string: paradox
Enter number of characters to mirror: 3
The result is: paizwlc
'''