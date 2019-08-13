import random


def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


li = list(range(1,10))
random.shuffle(li)
print('li:', li)
print(insertion_sort(li))
