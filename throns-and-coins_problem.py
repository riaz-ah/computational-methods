def thrones_and_coins(n, path):

    i=0
    x=n
    while i< n-1:
        if path[i]=="*" and path[i+1]=="*":
            x=i
            break
        else:
            i+=1

    return path[:x].count("@")

t= int(input())

for _ in range(t):
    n=int(input())
    path= input().strip()
    print(thrones_and_coins(n, path))


