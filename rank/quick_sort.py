'''
@Author: haikuoxin  
@Date: 2020-11-19 06:10:49  
@Last Modified by:   haikuoxin  
@Last Modified time: 2020-11-19 06:10:49 
'''

'''
双边循环快排法
'''
def quick_sort_v1(start_index, end_index, array=[]):
    if start_index >= end_index:
        return

    pivot_index = partition_v1(start_index, end_index, array)
    quick_sort_v1(start_index, pivot_index - 1, array)
    quick_sort_v1(pivot_index + 1, end_index, array)

def partition_v1(start_index, end_index, array=[]):
    pivot = array[start_index]
    left = start_index
    right = end_index
    while left != right:
        while left < right and array[right] > pivot:
            right -= 1
        while left < right and array[left] < pivot:
            left += 1
        if left < right:
            p = array[left]
            array[left] = array[right]
            array[right] = p
    array[start_index] = array[left]
    array[left] = pivot
    return left


'''
单边循环快排法
'''
def quick_sort_v2(start_index, end_index, array=[]):
    if start_index >= end_index:
        return
    pivot_index = partition_v2(start_index, end_index, array)
    quick_sort_v2(start_index, pivot_index - 1, array)
    quick_sort_v2(pivot_index + 1, end_index, array)

def partition_v2(start_index, end_index, array=[]):
    pivot = array[start_index]
    mark = start_index
    for i in range(start_index+1, end_index+1):
        if array[i] < pivot:
            mark += 1
            p = array[mark]
            array[mark] = array[i]
            array[i] = p
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark


if __name__ == "__main__":
    # 双边循环
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    quick_sort_v1(0, len(my_array) - 1, my_array)
    print(my_array)

    # 单边循环
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    quick_sort_v1(0, len(my_array) - 1, my_array)
    print(my_array)