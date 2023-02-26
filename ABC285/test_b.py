import unittest
import prog_b


class MyTestCase(unittest.TestCase):
    def test_01(self):
        string = "abcbac"
        string_length = len(string)

        result_list = prog_b.get_uncommon(string_length, string)
        self.assertEqual([5, 1, 2, 0, 1], result_list)


if __name__ == "__main__":
    unittest.main()

# EOF
