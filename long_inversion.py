def long_inversion(n, lst):

    if sum(lst)==0:
        return n
    elif n%2==1:
        for i in range((n//2), -1,-1):
            if lst[i]==1:
                return i+1
            else:
                break

    else:
        for i in range((n//2)-1, -1,-1):
            if lst[i]==1:
                return i+1
            break
    return i


t=int(input())

for _ in range(t):
    n=int(input())
    lst= list(map(int, input().split()))
    print(long_inversion(n,lst))

