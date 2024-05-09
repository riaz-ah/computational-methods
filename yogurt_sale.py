def yogurt_sale(n,a,b):
    if 2*a>b:
        min_cost=int((n//2)*b +(n%2)*a)
    else:
        min_cost=int(n*a)
    return min_cost


t=int(input())

for _ in range(t):
    n, a, b= map(int, input().split())
    print(yogurt_sale(n,a,b))
