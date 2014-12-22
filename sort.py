fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if not word in lst:
            lsts = lst.append(word)
lsts.sort()
print lsts