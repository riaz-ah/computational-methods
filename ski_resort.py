# a=k, b=n
def summation_function(a, b):
    total_sum = 0
    if a > b:
        return 0
    else:
        for i in range(a, b + 1):
            total_sum = total_sum + (b - i + 1)
        return total_sum

def ski_resort(k, q):
    count = 0
    grand_sum = 0
    lst2 = []
    for i in range(len(lst)):
        if lst[i] <= q:
            count = count + 1
        else:
            lst2.append(count)
            count = 0
    lst2.append(count)
    for i in lst2:
        grand_sum = grand_sum + summation_function(k, i)
    return grand_sum


t = int(input())

for i in range(t):
    n, k, q = map(int, input().split())
    lst = list(map(int, input().split()))
    print(ski_resort(k, q))
