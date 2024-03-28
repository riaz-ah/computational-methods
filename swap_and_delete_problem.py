def swap_and_delete(lst):
    n = len(lst)
    count0 = 0
    for i in range(n):
        if lst[i] == 0:
            count0 += 1
    count1 = n - count0

    x = 0
    while count1 > 0 and count0 > 0:
        if count1!=count0:
            if lst[i] == 0:
                count0 -= 1
                x += 1
            else:
                count1 -= 1
                x += 1
        else:
            return 0


    return n - x

# I just need to account the equal no of 1 and 0 case



t = int(input())

for _ in range(t):
    lst = list(map(int, input().split()))
    print(swap_and_delete(lst))
