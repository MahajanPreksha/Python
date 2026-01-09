cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)

elif selling_price == cost_price:
    print("No Profit, No Loss")

else:
    loss = cost_price - selling_price
    print("Loss:", loss)

'''Output:
Enter the cost price: 10
Enter the selling price: 20
Profit: 10
'''