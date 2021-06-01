# heapify a node
def heapify_node(heap, i):
    n = len(heap) - 1
    v = heap[i]

    p = i
    while p * 2 <= n:
        c = p * 2
        if p * 2 + 1 <= n and heap[c] > heap[p * 2 + 1]:
            c = p * 2 + 1
        
        if v > heap[c]:
            heap[p] = heap[c]
            p = c
        else:
            break
    heap[p] = v

# list to heap
def heapify_list(_list):
    _list.insert(0, 0)
    n = len(_list) - 1
    for i in range(n // 2, 0, -1):
        heapify_node(_list, i)
    
# push v to heap
def heap_push(heap, v):
    heap.append(v)
    i = len(list) - 1

    while i // 2 >= 1:
        if v < heap[i // 2]:
            heap[i] = heap[i // 2]
            i = i // 2
        else:
            heap[i // 2] = v
            break

# pop item from heap
def heap_pop(heap):
    n = len(heap) - 1
    if n <= 0:
        return -1

    ret_val = heap[1]
    
    heap[1] = heap[n]
    heap.pop()
    if n > 1:
        heapify_node(heap, 1)

    return ret_val

# heap sort
# return new list
def heap_sort(_list):
    ret_list = []
    heapify_list(_list)
    
    for i in range(len(_list) - 1):
        ret_list.append(heap_pop(_list))
    
    return ret_list
