from main_b import func
import unittest


class MyTestCase(unittest.TestCase):
    def test_func1(self):
        r = func(0, 0)
        self.assertEqual(r, 1)

    def test_func2(self):
        r = func(0, 0)
        self.assertEqual(r, 1)


class TestStdFunc(unittest.TestCase):
    def test_range(self):
        self.assertEqual([2, 3, 4], [x for x in range(2, 5)])

    def test_mod(self):
        self.assertEqual(3, 8 % 5)

    def test_divmod(self):
        self.assertEqual((1, 3), divmod(8, 5))

    def test_format_zero_padding(self):
        self.assertEqual("01", format(1, "0>2"))


if __name__ == '__main__':
    unittest.main()
