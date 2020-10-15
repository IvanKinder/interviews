import unittest
from multidel import multidel_v2


class unitTest(unittest.TestCase):
    def test_multidel(self):
        self.assertEqual(multidel_v2([1, 2, 5, 1, 7]), [1, 2, 5, 7])


if __name__ == "__main__":
    unittest.main()
