import unittest
from utils import dealArgs, cleanWord


args = [
    '--input=small_test.txt',
    '--start=foo',
    '--stop=bar',
    '--finish=enough',
    '--output=output.txt',
    '-s',
    '-f',
]


class UtilsTest(unittest.TestCase):
    def test_deal_args(self):
        res = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
            'format': False,
            'output': 'output.txt',
            # "stats" overrides "format"
            'stats': True,
        }
        self.assertEqual(res, dealArgs(args))

    def test_deal_no_args(self):
        self.assertRaises(ValueError, dealArgs, [])


    def test_clean_word(self):
        arr = ['@##it(#)', '\'"is#', '(($(`+)=-t1me{};<>?,./', 'for', 'A11', ' g00d ', '4', '!@#$%^&*()', ' ']
        res = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '', '']
        cleaned = []
        for word in arr:
            cleaned.append(cleanWord(word))
        self.assertEqual(res, cleaned)

if __name__ == '__main__':
    unittest.main()

