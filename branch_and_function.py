from sys import exit

def gold_room():
    print "enter a number?"
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("type a number")

    if how_much < 50:
        exit(0)
    else:
        dead("bad")
def bear_room():
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("face off")

        elif next == "taunt bear" and not bear_moved:
            print "go through"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("crotch off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "no idea"

def cthulu_room():
    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("well")
    else:
        cthulu_room()

def dead(why):
    print why, "Good job"
    exit(0)

def start():
    next = raw_input("> ")
    if next =="left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("stumble")

start()




