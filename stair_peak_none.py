def stair_peak_none(a,b,c):
    if a<b<c:
        return "STAIR"
    elif a<b>c:
        return "PEAK"
    else:
        return "NONE"


t=int(input())

for _ in range(t):
    a,b,c=map(int, input().split())
    print(stair_peak_none(a,b,c))