import unittest
from time import time
from index import dealArgs, getAndFilter

options = {'start': 'foo', 'stop': 'bar', 'finish': 'enough'}
words = [
    'fish',
    'hat',
    'foo',
    'cow',
    'siamese',
    'wonderland',
    'foo',
    'toothpaste',
    'bar',
    'umbrella',
    'foo',
    'milky',
    'flight-manual',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar'
]


args = [
    '-file=small_test.txt',
    '-start=foo',
    '-stop=bar',
    '-finish=enough',
]


class GetAndFilterTest(unittest.TestCase):
    def test_args_print(self):
        res = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
        }
        self.assertEqual(res, dealArgs(args))

    def test_speed_with_moby(self):
        t0 = time()
        mobyArgs= [
            '-file=moby_test.txt',
            '-start=whale',
            '-stop=mast',
            '-finish=ffff9999',
        ]
        self.assertGreater(207000, len(getAndFilter(mobyArgs)))
        t1 = time()
        print('Moby total get & parse time sec:', t1 - t0)


    def test_get_and_filter_simple(self):
        res = [
            'cow',
            'siamese',
            'wonderland',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        self.assertEqual(getAndFilter(args), res)


if __name__ == '__main__':
    unittest.main()

