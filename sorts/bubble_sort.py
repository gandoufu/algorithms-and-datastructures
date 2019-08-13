import random


def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
    return arr


li = list(range(1,10))
random.shuffle(li)
print('li:', li)
print(bubble_sort(li))

