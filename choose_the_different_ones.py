#
def check_fun1(arr1,arr2, k):
    arr1=sorted(arr1)
    lst1=[]
    for i in range(len(arr1)):
        if arr1[i]<=k:
            lst1.append(arr1[i])
    lst1 = list(set(lst1))



    arr2= sorted(arr2)
    lst2 = []
    for i in range(len(arr2)):
        if arr2[i] <= k:
            lst2.append(arr2[i])
    lst2= list(set(lst2))

    lst3=[]
    var="NO"
    if len(lst1)>=k/2 and len(lst2)>=k/2:
        lst_set3 = set(lst1 + lst2)

        if len(lst_set3)>=k:
            var= 'YES'
    else:
        var ="NO"



    return var



t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(check_fun1(arr1,arr2,k))


