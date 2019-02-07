import unittest
import walkArray

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

class WalkArrayTest(unittest.TestCase):
    def test_constructor(self):
        w = walkArray.WalkArray(words, options)
        self.assertEqual(w.words, words)

    def test_filter_simple(self):
        res = [
            'cow',
            'siamese',
            'wonderland',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        w = walkArray.WalkArray(words, options)
        w.filter()
        self.assertEqual(w.words, res)

    def test_filter_sudden_stop(self):
        words = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'enough',
            'trampoline',
            'apollo',
        ]
        res = [
            'fish',
            'flamingo',
        ]
        w = walkArray.WalkArray(words, options)
        w.filter()
        self.assertEqual(w.words, res)

    def test_filter_run_out(self):
        words = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        res = [
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        w = walkArray.WalkArray(words, options)
        w.filter()
        self.assertEqual(w.words, res)

if __name__ == '__main__':
    unittest.main()

