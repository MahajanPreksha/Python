def fibo(n):
    #Base Cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2) #Recursive Case
    
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(fibo(i))

'''Output:
Enter n: 7
0
1
1
2
3
5
8
'''