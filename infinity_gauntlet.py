dic = {"Power": "purple", "Time": "green", "Space": "blue", "Soul": "orange", "Reality": "red", "Mind": "yellow"}

def get_key_from_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None  # Value not found in the dictionary
def infinity_gauntlet():
    lst2=[]
    lst3=["Power", "Time", "Space", "Soul", "Reality", "Mind"]
    # print(6-n)
    for i in lst:

        lst2.append(get_key_from_value(dic,i))
    for i in lst2:
        if i in lst3:
            lst3.remove(i)
    return lst3


n= int(input())
lst = []
for i in range(n):
    if n>6:
        print('n greater than 6')
        exit()
    else:
        lst.append(input())

lst2= infinity_gauntlet()
print(6-n)
for i in lst2:
    print(i)

