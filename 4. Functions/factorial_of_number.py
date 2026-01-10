#Function for calculating factorial of a number
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *=i
    return ans
    
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))

'''Output:
Enter a number: 5
Factorial of 5 is 120
'''