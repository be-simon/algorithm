
def swap(_list, i, j):
    _list[i], _list[j] = _list[j], _list[i]

def bubble_sort(_list):
    n = len(_list)

    for i in range(n):
        for j in range(n - i - 1):
            if _list[j] > _list[j + 1]:
                swap(_list, j, j + 1)

    return _list

def selection_sort(_list):
    n = len(_list)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if _list[j] < _list[min_idx]:
                min_idx = j
        swap(_list, i, min_idx)

    return _list        


def insertion_sort(_list):
    n = len(_list)
    for i in range(1, n):
        v = _list[i]
        idx = 0
        for j in range(i - 1, -1, -1):
            if v < _list[j]:
                _list[j + 1] = _list[j]
            else:
                idx = j + 1
                break
        _list[idx] = v
    
    return _list
