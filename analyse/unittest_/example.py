import unittest

from my_package.my_module import my_pow


class TestMyModule(unittest.TestCase):
    def test_my_pow(self):
        self.assertEqual(my_pow(2, 2), 4)
        self.assertEqual(my_pow(4, 8), pow(4, 8))


if __name__ == '__main__':
    unittest.main()
