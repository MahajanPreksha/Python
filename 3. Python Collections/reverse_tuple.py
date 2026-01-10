n = int(input("Enter the size of the tuple: "))

li = []
for _ in range(n):
    element = input("Enter element: ")
    li.append(element)

tup = tuple(li)
print("Original Tuple:", tup)

rev_li = []
for i in reversed(tup):
    rev_li.append(i)

rev_tup = tuple(rev_li)
print("Reversed Tuple:", rev_tup)

'''Output:
Enter the size of the tuple: 4
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Original Tuple: ('1', '2', '3', '4')
Reversed Tuple: ('4', '3', '2', '1')
'''