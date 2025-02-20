def factorial(n):
    if n==0: #Base Case
        return 1
    else:
        return n * factorial(n-1) #Recursive Case
    
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))