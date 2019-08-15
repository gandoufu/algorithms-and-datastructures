def merge(arr_a, arr_b):
    '''合并两个有序序列为一个有序序列'''
    i = 0
    j = 0
    new_arr = []
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] <= arr_b[j]:
            new_arr.append(arr_a[i])
            i += 1
        else:
            new_arr.append(arr_b[j])
            j += 1
    # 判断哪个序列中有剩余元素，将其加入到新的数组中
    if i < len(arr_a):
        new_arr += arr_a[i:]
    if j < len(arr_b):
        new_arr += arr_b[j:]
    return new_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
