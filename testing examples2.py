from nose.tools import *
from ex13 import Room

def test_room():
    gold = Room('GlodRoom', "this room has gold in it you can grab.")
    assert_equal(gold.name, 'GlodRoom')
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room('center', 'in the center.')
    north = Room('North', 'in the north.')
    south = Room('South', 'in the south.')

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room('Start', 'down a hole.')
    west = Room('Trees', 'There are trees here you can go east.')
    down = Room('Dungeon', 'you can go up.')

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)