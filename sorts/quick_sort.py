# 方法一
def quick_sort(arr, left, right):
    if left >= right:
        return
    low = left
    high = right
    pivot = arr[low]
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[right] = pivot
    quick_sort(arr, low, left-1)
    quick_sort(arr, left+1, high)


# 方法二
def _quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    smaller_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return _quick_sort(smaller_than_pivot) + [pivot] + _quick_sort(greater_than_pivot)
