import random


def selection_sort(arr):
    for i in range(len(arr)-1):
        smallest_ele_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_ele_index]:
                smallest_ele_index = j
        arr[i], arr[smallest_ele_index] = arr[smallest_ele_index], arr[i]
    return arr


li = list(range(1,10))
random.shuffle(li)
print('li:', li)
print(selection_sort(li))
