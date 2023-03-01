import unittest
import prog_c


class MyTestCase(unittest.TestCase):
    def test_01(self):
        string_id = "A"
        value_id = prog_c.decode(string_id)
        self.assertEqual(1, value_id)

        string_id = "Z"
        value_id = prog_c.decode(string_id)
        self.assertEqual(26, value_id)

        string_id = "AA"
        value_id = prog_c.decode(string_id)
        self.assertEqual(27, value_id)

        string_id = "AB"
        value_id = prog_c.decode(string_id)
        self.assertEqual(28, value_id)

        string_id = "AZ"
        value_id = prog_c.decode(string_id)
        self.assertEqual(52, value_id)

        string_id = "BA"
        value_id = prog_c.decode(string_id)
        self.assertEqual(53, value_id)


if __name__ == "__main__":
    unittest.main()

# EOF
