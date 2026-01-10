#Creating a function
def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a number: "))

#Calling the function
print("Sum of all numbers till n:", sum(n))

'''Output:
Enter a number: 4
Sum of all numbers till n: 10
'''