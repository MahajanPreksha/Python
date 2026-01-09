num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator: ")

match operator:
    case "+":
        print("Sum is:", num1 + num2)
    case "-":
        print("Difference is:", num1 - num2)
    case "*":
        print("Product is:", num1 * num2)
    case "/":
        print("Division is:", num1 / num2)
    case "_":
        print("Enter a valid operator!")

'''Output:
Enter first number: 3
Enter second number: 4
Enter operator: +
Sum is: 7
'''