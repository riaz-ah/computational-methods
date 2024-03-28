def make_equal_again(n, arr):
    if (arr[0]==arr[n-1]):
        i = 0
        x = 0
        j = n - 1
        y = 0
        while i <= n - 1:
            if arr[i] == arr[0]:
                x += 1
                i += 1
            else:
                break

        while j >= 0:
            if arr[j] == arr[n - 1]:
                y += 1
                j -= 1
            else:
                break
        if x + y>=n:
            return 0
        else:
            return n-(x+y)
    else:
        i = 0
        x = 0
        j = n - 1
        y = 0
        while i <= n - 1:
            if arr[i] == arr[0]:
                x += 1
                i += 1
            else:
                break

        while j >= 0:
            if arr[j] == arr[n - 1]:
                y += 1
                j -= 1
            else:
                break
        return (n-max(x,y))






t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(make_equal_again(n, arr))
