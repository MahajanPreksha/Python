def f(n):
    if n==0:
        return
    f(n-1)
    print(n)

n = int(input("Enter n: "))
f(n)