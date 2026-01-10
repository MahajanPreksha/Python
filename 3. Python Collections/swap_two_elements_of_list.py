n = int(input("Enter the size of the list: "))

li = []
for _ in range(n):
    num = int(input("Enter element: "))
    li.append(num)

print("Original list:", li)

idx1 = int(input("Enter the first index to swap: "))
idx2 = int(input("Enter the second index to swap: "))

temp = li[idx1]
li[idx1] = li[idx2]
li[idx2] = temp

print("List after swapping:", li)

'''Output:
Enter the size of the list: 5
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Original list: [1, 2, 3, 4, 5]
Enter the first index to swap: 2
Enter the second index to swap: 4
List after swapping: [1, 2, 5, 4, 3]
'''