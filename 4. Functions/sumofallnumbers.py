def sum(n): #Creating a function
    sum = 0
    for i in range(1, n+1):
        sum +=i
    return sum

n = int(input("Enter a number: "))
print("Sum of all numbers till n:", sum(n)) #Calling the function