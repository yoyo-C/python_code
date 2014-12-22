the_count = [1,2,3,4,5]
fruits = ['apple', "oranges",'pears','apricots']
change = [1,'pennies', 2, "dimes", 3, 'quarters']

for num in the_count:
    print "%d" % num

for fruit in fruits:
    print "%s" %fruit

for n in change:
    print "%r" %n

element = []
for i in range(0,6):
    print "%d" % i
    element.append(i)

for i in element:
    print '%d' % i