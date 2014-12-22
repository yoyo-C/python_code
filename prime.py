import math
import unittest

def is_prime(i):
    try:
        i = int(i)
    except:
        print "oops!!!not a integer,hahaha"
        return None

    if i < 2:
        return False
    elif i == 2:
        return True
    else:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0 :
                return False
        return True

class TestIsPrime(unittest.TestCase):
    def test2(self):
        self.assertTrue(is_prime(2))

    def test3(self):
        self.assertTrue(is_prime(3))

    def testsdfadfaeg(self):
        self.assertFalse(is_prime(4))

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsPrime)
    unittest.TextTestRunner(verbosity=2).run(suite)