ten_things = "A O C T L S"
print "wait, not 10 things, fix this!"

stuff = ten_things.split(' ')

more_stuff = ['d','n','s','f','c','b','g','bo']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print next_one
    stuff.append(next_one)
    print len(stuff)

print stuff

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])




