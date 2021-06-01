

# merge left & right list
def merge(l_list, r_list):
    ret_list = []
    li = 0
    ri = 0

    while li < len(l_list) and ri < len(r_list):
        if l_list[li] < r_list[ri]:
            ret_list.append(l_list[li])
            li += 1
        else:    
            ret_list.append(r_list[ri])
            ri += 1
    
    while li < len(l_list):
        ret_list.append(l_list[li])
        li += 1
    
    while ri < len(r_list):
        ret_list.append(r_list[ri])
        ri += 1

    return ret_list

# merge sort
# recursive function
def merge_sort(_list):
    n = len(_list)
    if n <= 1:
        return _list

    m = n // 2
    
    l_list = merge_sort(_list[:m])
    r_list = merge_sort(_list[m:])

    return merge(l_list, r_list)
