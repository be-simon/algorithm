from simple_sort import swap

def _partition(_list, left, right):
    p = (left + right) // 2
    pivot = _list[p]
    swap(_list, left, p)

    high = right
    low = left + 1

    while low < high:
        while _list[high] > pivot and high > left:
            high -= 1
        while _list[low] < pivot and low < right:
            low += 1
        
        if low < high:
            swap(_list, low, high)
        else:
            break
    swap(_list, left, high)
    return p

def _quick_sort(_list, left, right):
    if left < right:
        p = _partition(_list, left, right)
        _quick_sort(_list, left, p - 1)
        _quick_sort(_list, p + 1, right)


def quick_sort(_list):
    _quick_sort(_list, 0, len(_list) - 1)
    return _list

