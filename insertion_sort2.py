def insertion_sort(n):
    if len(n) == 1:
        return n
    b = insertion_sort(n[1:])
    m = len(b)
    for i in range(m):
        if n[0] <= b[i]:
            return b[:i]+[n[0]]+b[i:]
    return b + [n[0]]

test_list = [2,5,32,27,98,17]
print insertion_sort(test_list)