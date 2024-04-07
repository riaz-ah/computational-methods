def max_the_score(n, lst):
    if len(lst) != 2 * n:
        return "invalid list input"
    else:
        srt_lst = sorted(lst)
        sum = 0
        for i in range(n):
            sum = sum + srt_lst[2 * i]
        return sum


t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(max_the_score(n, lst))
