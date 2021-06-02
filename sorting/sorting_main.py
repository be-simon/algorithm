from quick_sort import quick_sort
import random
import timeit
from simple_sort import bubble_sort
from simple_sort import selection_sort
from simple_sort import insertion_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort

MAX_LIST_LEN = 15
MAX_LIST_ITEM_VAL = 100
MIN_LIST_ITEM_VAL = 0


def get_random_list():
    # _size = random.randint(5, 20)
    _size = MAX_LIST_LEN
    _list = []

    for i in range(_size):
        _list.append(random.randint(MIN_LIST_ITEM_VAL, MAX_LIST_ITEM_VAL))
    
    return _list



sort_algos = [bubble_sort, selection_sort, insertion_sort, merge_sort, heap_sort, quick_sort]

for algo in sort_algos:
    _list = get_random_list()
    print(algo.__name__)
    print('before : ', _list)
    print('after : ', algo(_list))
    algo_time = timeit.timeit(lambda: algo(_list), number=200000)
    print('time : ', round(algo_time, 5))
    print('-' * 10)
