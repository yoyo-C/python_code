def bubble(list):
    for j in range(len(list) - 1, 0, -1):
        for i in range(0, j):
            if list[i] > list[i + 1]: list[i], list[i + 1] = list[i + 1], list[i]
    return list

testlist = [22, 2, 1, 34, 76, 122]
print ('final:', bubble(testlist))