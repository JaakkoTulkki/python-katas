def chop(item, sorted_array):
    if not sorted_array:
        return -1

    first = 0
    last = len(sorted_array) - 1

    while first <= last:
        mid_point = (first + last) // 2
        mid_item = sorted_array[mid_point]

        if item == mid_item:
            return mid_point
        if item < mid_item:
            last = mid_point - 1
        if item > mid_point:
            first = mid_point + 1
    return -1

