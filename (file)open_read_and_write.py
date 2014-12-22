from sys import argv

script, filename = argv
target = open(filename, 'w')

print 'going to truncate'
target.truncate()

print 'ask for 3line.'

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")


print "going to write."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "going to finish"
target.close()