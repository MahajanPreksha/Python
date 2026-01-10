def f(n):
    if n == 0:
        return
    print(n)
    f(n - 1)

n = int(input("Enter n: "))

f(n)

'''Output:
Enter n: 5
5
4
3
2
1
'''