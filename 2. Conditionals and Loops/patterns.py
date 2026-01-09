#Pattern - 1
n = int(input())

for i in range(1, n + 1):
    print("*" * 5)

'''Output:
4
*****
*****
*****
*****
'''

#Pattern - 2
m = int(input())
for _ in range(m):
    for i in range(1, m + 1):
        print(i, end="")
    print()

'''Output:
4
1234
1234
1234
1234
'''

#Pattern - 3
x = int(input())
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

'''Output:
4
1
12
123
1234
'''

#Pattern - 4
y = int(input())
for i in range(1, y + 1):
    print(" " * (y - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()

'''Output:
4
   1
  123
 12345
1234567
'''