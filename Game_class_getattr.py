from sys import exit
from random import randint

class Game(object):
    def __init__(self, start):
        self.quips = ['you kinda suck at this.', 'your mom would proud.','such a luse.','i have a small puppy']
        self.start = start

    def play(self):
        next = self.start

        while True:
            print '\n----------'
            room = getattr(self, next)
            next = room()

    def death(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)

    def princess_lives_here(self):
        print 'she offers you some cake.'

        eat_it = raw_input("> ")
        if eat_it == "eat it":
            print 'the princess cackles and eats the frogs'
            return 'death'

        elif eat_it == 'do not eat it':
            print 'she throws the cake at you'
            return 'death'

        elif eat_it == 'make her eat it':
            print 'she gives you the very last bit of cake'
            return 'gold_koi_pond'

        else:
            print 'the princess looks at you confused'
            return 'princess_lives_here'

    def gold_koi_pond(self):
        print 'it opens its mouth waiting for you'
        feed_it = raw_input('> ')

        if feed_it == 'feed it':
            print 'you are the pooped out sometime later.'
            return 'death'

        elif feed_it == 'do not feed it':
            print 'you are then pooped out a week later.'
            return 'death'

        elif feed_it == 'throw it in':
            print 'at your feet.'
            return 'bear_with_sword'

        else:
            print 'the koi gets annoyed and viggles a bit.'
            return 'gold_koi_pond'

    def bear_with_sword(self):
        print 'it holds its paw out and looks at you.'
        give_it = raw_input("> ")

        if give_it == 'give it':
            print 'the last thing you see is the bear shrug and eat you.'
            return 'death'

        elif give_it == 'say no':
            print 'where the hell did that come from?'
            return 'big_iron_gate'

    def big_iron_gate(self):
        print 'you walk up to the big iron gate and see there'
        open_it = raw_input("> ")

        if open_it == 'open it':
            print 'you open it and you are free!'
            return 'death'

        else:
            print 'the doesn\'t sees sensible'
            return 'big_iron_gate'

a_game = Game("princess_lives_here")

a_game.play()

