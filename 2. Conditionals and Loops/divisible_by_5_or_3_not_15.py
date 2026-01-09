num = int(input("Enter a positive integer: "))

if num % 15 == 0:
    print("Divisible by 15.")
else:
    if num % 3 == 0 or num % 5 == 0:
        print("Divisible by 3 or 5 but not 15.")
    else:
        print("Not divisible by 3 or 5.")

'''Output:
Enter a positive integer: 20
Divisible by 3 or 5 but not 15.
'''