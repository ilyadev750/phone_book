import unittest
import re
from phonebook import PhoneBook

RAW_STRING = '       Иванов        |      Иван       |       Иванович        |       Сбербанк        |    845632547    |     789634      |\n'
LIST_DATA = [1, 'Иванов', 'Иван', 'Иванович', 'Сбербанк', '845632547', '789634', ''] 

class TestBook(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook(filename='test_phonebook.txt')

    def get_info_from_file(self):
        with open(self.phonebook.filename, 'r') as phonebook:
            for i, line in enumerate(phonebook, 1):
                if i == self.phonebook.line_number:
                    self.phonebook.all_filestrings.append(line)
                    self.phonebook.line_number += 3
                else:
                    continue

    def test_get_string_from_file(self):
        self.get_info_from_file()
        self.assertEqual(self.phonebook.all_filestrings[0], RAW_STRING)

    def test_convert_string_into_list_for_printing(self):
        self.get_info_from_file()
        line = self.phonebook.all_filestrings[0]
        line = line.replace('|', ' ')
        line = re.sub('\s{2,}', '  ', line)
        line = list(line.split("  "))
        line[0] = 1
        self.assertEqual(line, LIST_DATA)

if __name__ == "__main__":
    unittest.main()