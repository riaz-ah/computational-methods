def tiles_comeback(k, lst):
    count = 0
    tracker = 0
    count_index = -1
    if lst[0] != lst[-1]:
        for i in range(len(lst)):
            if lst[i] == lst[0]:
                count += 1
                count_index = i
                if count >= k:
                    break


        for j in range(len(lst) - 1, count_index, -1):
            if lst[j] == lst[-1]:
                tracker += 1
                if tracker >= k:
                    break


        if count>=k and tracker>=k:
            return "YES"
        else:
            return "NO"

    else:
        for i in range(len(lst)):
            if lst[i] == lst[0]:
                count += 1
        if count >= k:
            return "YES"
        else:
            return "NO"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(tiles_comeback(k, lst))
