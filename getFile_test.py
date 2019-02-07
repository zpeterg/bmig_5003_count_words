import unittest
from time import time
from getFile import getFile

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


class GetFileTest(unittest.TestCase):
    def test_getFile_basic(self):
        self.assertEqual(words, getFile('small_test.txt'))

    def test_getFile_no_file(self):
        self.assertRaises(FileNotFoundError, getFile, 'aaa.txt')

    def test_getFile_moby(self):
        t0 = time()
        self.assertLess(200000, len(getFile('moby_test.txt')))
        t1 = time()
        print('Moby import time sec:', t1 - t0)


if __name__ == '__main__':
    unittest.main()