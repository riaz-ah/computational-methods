import math


def max_ones(n,k):
    arr=[]

    if math.log2(k) == int(math.log2(k)):
        if n == 1:
            arr.append(k)
        if n == 2:
            arr.append(k-1)
            arr.append(1)
        if n>2:
            arr.append(k - 1)
            arr.append(1)
            for i in range(2, n):
                arr.append(0)
    else:
        var = math.log2(k)
        # print(var)
        var = math.floor(var)
        var = (2 ** var) - 1
        num = k - var
        # print(bin(var))
        if n == 1:
            arr.append(k)
        if n == 2:
            arr.append(var)
            arr.append(num)
        if n>2:
            arr.append(var)
            arr.append(num)
            for i in range(2, n):
                arr.append(0)
    return arr


t=int(input())
for i in range(t):
    n,k= map(int,input().split())
    result = max_ones(n, k)
    print(*result, end=' ')
    print()

