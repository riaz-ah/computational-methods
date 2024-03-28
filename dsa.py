import numpy as np
import math

def median_of_an_array(list_of_numbers):
    count=0
    new_list_of_numbers= sorted(list_of_numbers)
    y=len(new_list_of_numbers)
    x = (y + 1) // 2 - 1  # Calculate the index of the median
    median= new_list_of_numbers[x]
    for i in range(x,y):
        if new_list_of_numbers[i]==median:
            count+=1
    return count


t=int(input())

for _ in range(t):
    n=int(input())
    list_of_numbers= list(map(int, input().split()))
    print(median_of_an_array(list_of_numbers))

