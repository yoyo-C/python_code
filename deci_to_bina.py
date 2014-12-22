# i = raw_input("a number:")
# i = int(i)

def dec_to_bin(i):
    try:
        i = int(i)
    except ValueError:
        print "Invalid input! Need a number."
        return None
    lst = []
    while True:
        if i <= 1:
            lst.append(i)
            break
        else:
            j = i % 2
            lst.append(j)
            i = i / 2
    lst.reverse()
    return "".join([str(x) for x in lst])
#[str(x) for x in lst]
print dec_to_bin(100)

def test_cases():
    assert(dec_to_bin(0) == '0')
    assert(dec_to_bin(1) == '1')
    assert(dec_to_bin(4) == '100')
    assert(dec_to_bin('a') == None)
    print 'all pass!'
#[str(x) for x in lst]
test_cases()