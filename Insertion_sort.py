def insertion_sort(lst):
    if len(lst) == 1:
        return lst
 
    for i in xrange(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp > lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

test_list = [2, 3, 5, 6, 9, 29, 1]
print insertion_sort(test_list)