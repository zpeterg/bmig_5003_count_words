import unittest
from os import remove
from writeFile import writeFile

file_name = 'temp_output_for_test.txt'
content = 'foo\nbar'


class WriteFileTest(unittest.TestCase):
    def test_file_write(self):
        writeFile(content, file_name)
        with open(file_name, 'r') as file:
            # append each line with a space

            self.assertEqual(content, file.read())

    def tearDown(self):
        remove(file_name)
