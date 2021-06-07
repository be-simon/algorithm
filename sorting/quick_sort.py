from simple_sort import swap

def _partition(_list, left, right):
    p = (left + right) // 2
    pivot = _list[p]
    swap(_list, left, p)

    high = right
    low = left

    while low < high:
        while high > left and _list[high] > pivot :
            high -= 1        
        while low < right and _list[low] <= pivot:
            low += 1

        if low < high:
            swap(_list, low, high)
        
    swap(_list, left, high)

    return high

def _quick_sort(_list, left, right):
    if left < right:
        p = _partition(_list, left, right)
        _quick_sort(_list, left, p - 1)
        _quick_sort(_list, p + 1, right)


def quick_sort(_list):
    _quick_sort(_list, 0, len(_list) - 1)
    return _list

