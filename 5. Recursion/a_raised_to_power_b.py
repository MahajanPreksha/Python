def f(a, b):
    if b==0:
        return 1
    else:
        return a * f(a, b-1)
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("a raised to power b is:", f(a, b))

'''Output:
Enter a: 3
Enter b: 2
a raised to power b is: 9
'''