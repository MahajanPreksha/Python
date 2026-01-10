def f(n):
    #Base Case
    if n == 1:
        return 1
    return n + f(n - 1) #Recursive Case

n = int(input("Enter n: "))

print("Sum of numbers till n:", f(n))

'''Output:
Enter n: 5
Sum of numbers till n: 15
'''