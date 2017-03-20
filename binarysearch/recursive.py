def chop(item, sorted_list):
    if not sorted_list:
        return -1

    mid_point = len(sorted_list) // 2
    found_item = sorted_list[mid_point]

    if item == found_item:
        return mid_point

    if item < found_item:
        return chop(item, sorted_list[:mid_point])

    found = chop(item, sorted_list[mid_point + 1:])
    if found < 0:
        return -1
    return mid_point + 1 + found
