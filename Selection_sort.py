def selection_sort(list):
    N = len(list)
    exchange_count = 0
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if list[min_index] > list[j]:
                min_index = j
        if min_index != i:
            list[min_index], list[i] = list[i], list[min_index]
            exchange_count += 1
    return list

testlist = [17,23,32,1,2,7,6,4,32,27,67]
print selection_sort(testlist)
