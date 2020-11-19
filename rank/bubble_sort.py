'''
@Author: haikuoxin  
@Date: 2020-11-12 07:00:09  
@Last Modified by:   haikuoxin  
@Last Modified time: 2020-11-12 07:00:09 
'''
def bubble_sort(array=[]):
    last_exchange_index = 0
    sort_border = len(array)
    for i in range(len(array)-1):
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_sorted = False
                last_exchange_index = j
        sort_border = last_exchange_index
        if is_sorted:
            break

def cock_tail_sort(array=[]):
    for i in range(len(array) // 2):
        
        # 奇数轮
        is_sorted = True
        for j in range(i, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_sorted = False
        if is_sorted:
            break

        # 偶数轮
        is_sorted = True
        for j in range(len(array)-i-1, i, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                is_sorted = False
        if is_sorted:
            break


if __name__ == "__main__":
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    cock_tail_sort(my_array)
    print(my_array)