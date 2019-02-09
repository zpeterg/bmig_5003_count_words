import unittest
from time import time
from index import getAndFilter


class GetAndFilterTest(unittest.TestCase):

    def test_speed_with_moby(self):
        t0 = time()
        options = {
            'file': 'moby_test.txt',
            'start': 'whale',
            'stop': 'mast',
            'finish': 'ffff9999',
        }
        self.assertLess(190000, len(getAndFilter(options)))
        t1 = time()
        print('Moby total get & parse time sec:', t1 - t0)


    def test_get_and_filter_simple(self):
        options = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
        }
        res = [
            'cow',
            'cow',
            'siamese',
            'wonderland',
            'foo',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        self.assertEqual(getAndFilter(options), res)


if __name__ == '__main__':
    unittest.main()

