from main_a import func
import unittest


class MyTestCase(unittest.TestCase):
    pass


class TestStdFunc(unittest.TestCase):
    def test_range(self):
        self.assertEqual([2, 3, 4], [x for x in range(2, 5)])

    def test_mod(self):
        self.assertEqual(3, 8 % 5)

    def test_divmod(self):
        self.assertEqual((1, 3), divmod(8, 5))

    def test_format_zero_padding(self):
        self.assertEqual("01", format(1, "0>2"))

    def test_list_index(self):
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual([1, 2], data[:2])
        self.assertEqual([2, 3, 4], data[1:4])
        self.assertEqual([4, 5, 6], data[-3:])
        self.assertEqual(6, data[-1])
        self.assertEqual(6, data.pop())
        self.assertEqual([1, 2, 3, 4, 5], data)

    def test_list_step(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        b = [0, 2, 4, 6, 8]
        self.assertEqual(a[::2], b)


if __name__ == '__main__':
    unittest.main()
