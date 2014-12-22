from sys import exit
from random import randint
def death():
    quips = ["you died, you kinda suck at this.", 'Your mom would be proud. If she were smarter.', 'such a luser.', 'I have a small puppy that\' better at this.']
    print quips[randint(0,len(quips)-1)]
    exit(1)

def princess_lives_here():
    print 'you see a beautiful princess with a shiny crown.'
    print 'she offers you some cake.'
    eat_it = raw_input("> ")

    if eat_it == "eat it":
        print "the princess cackles and eats the frogs. Yum!"
        return 'death'

    elif eat_it == "do not eat it":
        print 'the last thing you see is her muching on your torso. Yum!'
        return 'death'

    elif eat_it == 'make her eat it':
        print 'then she smiles and cries and thanks yu for saving her.'
        return 'gold_koi_pond'

    else:
        print 'the princess looks at you confused and just points at the cake.'
        return 'princess_lives_here'


def gold_koi_pond():
    print 'It opens its mouth waiting for food.'

    feed_it = raw_input("> ")

    if feed_it == "feed it":
        print 'you are then pooped out stime later.'
        return 'death'

    elif feed_it == 'do not feed it':
        print 'you are then pooped out a week later.'
        return 'death'

    elif feed_it == 'throw it in':
        print 'at your feet.'
        return 'bear_with_sword'

    else:
        print 'the koi gets annoyed and wiggles a bit.'
        return 'gold_koi_pond'

def bear_with_sword():
    print 'it holds its paw out and looks at you.'

    give_it = raw_input("> ")

    if give_it == "give it":
        print 'the last thing you see is the bear shrug and eat you.'
        return 'death'

    elif give_it == 'say no':
        print 'where the hell did that come from? you say.'
        return 'big_iron_gate'

    else:
        print 'the bear look puzzled as to why you\'d do that.'
        return 'bear_with_sword'

def big_iron_gate():
    print 'you walk up to the big iron gate and see there\'s a handle.'

    open_it = raw_input("> ")

    if open_it == 'open it':
        print 'who\'s laughing now!? love this katana.'
        return 'death'

    else:
        print 'that dosen\'t seem sensible. i mean, the door\'s right here.'
        return 'big_iron_gate'

ROOMS = {
    'death': death, 
    'princess_lives_here':princess_lives_here, 
    'gold_koi_pond': gold_koi_pond, 
    'bear_with_sword': bear_with_sword,
    'big_iron_gate': big_iron_gate
}

def runner(map, start):
    next = start
    while True:
        room = map[next]
        print room
        print '\n--------------'
        next = room()
        print next

runner(ROOMS, 'princess_lives_here')