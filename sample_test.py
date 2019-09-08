import unittest
from sample_package.sub_package1 import my_sum


class TestSamplePackage(unittest.TestCase):
    def test_my_sum(self):
        self.assertEqual(my_sum([7,9,1]),17)

if __name__ == '__main__':
    unittest.main()
