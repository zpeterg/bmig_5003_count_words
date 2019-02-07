import unittest
from cleanWords import cleanWords

arr = ['foo', 'bar', 'fish', 'stapler', 'anchovies', 'falcon-heavy', 'saffron', 'waterfall']

class FormatTest(unittest.TestCase):
    def test_clean_words(self):
        arr = ['@##it(#)', '\'"is#', '(($(`+)=-t1me{};<>?,./', 'for', 'A11', ' g00d ', '!@#$%^&*()', ' ']
        res = ['it', 'is', 't1me', 'for', 'A11', 'g00d']
        self.assertEqual(res, cleanWords(arr))

if __name__ == '__main__':
    unittest.main()

