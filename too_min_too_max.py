
def too_min_too_max(n, arr):
    if len(arr) < 4:
        return "array too short"
    else:
        srt_arr = sorted(arr)
    sum = abs(srt_arr[0] - srt_arr[n - 1]) + abs(srt_arr[1] - srt_arr[n - 2]) \
          + abs(srt_arr[0] - srt_arr[n - 2]) + abs(srt_arr[1] - srt_arr[n - 1])
    return sum

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(too_min_too_max(n, arr))
