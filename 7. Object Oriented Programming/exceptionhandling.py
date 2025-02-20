a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    result = a/b
except ZeroDivisionError:
    result = None
    print("Error: Can't divide by zero")
finally:
    print("Division operation completed: ", result)