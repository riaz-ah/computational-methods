


def moving_chips(n, lst):
    initial_index = -1
    final_index = -1
    count = 0

    for i in range(n):
        if lst[i] == 1:
            initial_index = i
            break

    for i in range(n - 1, -1, -1):
        if lst[i] == 1:
            final_index = i
            break

    for i in range(initial_index, final_index):
        if initial_index==final_index:
            return 0
        else:
            if lst[i] == 0:
                count = count + 1

    return count


t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(moving_chips(n, lst))
