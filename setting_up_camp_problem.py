def setting_up_camp(a,b,c):
    n=b%3
    m=n+c
    if n!=0 and 0<m<3:
        return (-1)
    if n==0 and 0<m<3:
        return (a+(b//3)+ 1)
    if m>=3 and m%3!=0:
        return(a+(b//3)+(m//3) + 1)
    else:
        return(a+(b//3)+(m//3))



t=int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    print(setting_up_camp(a,b,c))




