# 查找算法，下面介绍：二分查找、三分查找

#############################################################
#######################  二分查找    ##########################
#############################################################
def second_search(arr, item):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        if mid_value == item:
            return mid
        elif mid_value < item:
            low = mid + 1
        elif mid_value > item:
            high = mid - 1
    return None


my_arr1 = [1, 4, 5, 6, 7, 8, 9, 66, 100]


# print(second_search(my_arr1, 100))

#############################################################
#######################  三分查找    ##########################
#############################################################
def third_search(arr, item):
    low = 0
    high = len(arr)
    while low + 1 < high:
        mid1 = (high - low) // 2 + low
        mid2 = high - (high - low) // 2
        if arr[mid1] == item:
            return mid1
        elif arr[mid2] == item:
            return mid2
        elif item < mid1:
            high = mid1 - 1
        elif item > mid2:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return None


my_arr2 = [1, 4, 5, 6, 7, 8, 9, 66, 100]
# print(third_search(my_arr2, 100))
