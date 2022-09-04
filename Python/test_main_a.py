from main_a import func
import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        ans = func("Wednesday")
        res = 3
        self.assertEqual(res, ans)

    def test_2(self):
        ans = func("Monday")
        res = 5
        self.assertEqual(res, ans)


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