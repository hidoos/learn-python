import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        fullname = get_formatted_name('hidoos', 'lan')
        self.assertEqual(fullname,'Hidoos Lan')

    def test_first_middle_last_name(self):
        fullname = get_formatted_name('hidoos', 'lan', 'mess')
        self.assertEqual(fullname,'Hidoos Mess Lan')

unittest.main()        

