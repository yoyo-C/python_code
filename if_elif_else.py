print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "enter 1 or 2"
    bear = raw_input("> ")
    if bear == "1":
        print "face"
    elif bear == "2":
        print "legs"
    else:
        print "%s" %bear

elif door == "2":
    print "enter 1, 2 or 3"
    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "mind"
    else:
        print "eye"

else:
    print "good job"