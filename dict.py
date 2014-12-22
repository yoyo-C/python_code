cities = {'CA': 'San','MI':'Det','FL':'Jack'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

while True:
    print "State? (ENTER to quit)",
    state = raw_input("> ")

    if not state:break

    print find_city(cities, state)





