import unittest
from typing import Any
import prog_a


g_data_dict: dict[Any, Any] = {}


class MyTestCase(unittest.TestCase):
    def setUp(self):
        global g_data_dict
        g_data_dict = prog_a.setup()

    def test_01(self):
        b_line = prog_a.is_line(g_data_dict, 1, 2)
        self.assertTrue(b_line)

        b_line = prog_a.is_line(g_data_dict, 2, 8)
        self.assertFalse(b_line)

        b_line = prog_a.is_line(g_data_dict, 14, 15)
        self.assertFalse(b_line)


if __name__ == "__main__":
    unittest.main()

# EOF
