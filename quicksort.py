step = 0

def quicksort(array):
    global step
    if len(array) <= 1: return array
    less, greater = [], []
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    step += 1
    print "step %s: less: %s, pivot: %s, greater: %s" % (step, less, pivot, greater)
    return quicksort(less) + [pivot] + quicksort(greater)

a = [1,3,8,6,8,0,3,6,9,9,7]

print quicksort(a)