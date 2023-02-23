import unittest
import prog_b


class MyTestCase(unittest.TestCase):
    def test_01(self):
        """ test 1
        0.1km 未満：
          VVの値は 00 とする。
        """
        input_data = 0
        output_data = prog_b.calc(input_data)
        self.assertEqual(0, output_data)

        input_data = 99
        output_data = prog_b.calc(input_data)
        self.assertEqual(0, output_data)

    def test_02(self):
        """ test 2
        0.1km 以上 5km 以下：
          距離 (km) を 10 倍した値とする。1 桁の場合は上位に 0 を付す。
        """
        input_data = 100
        output_data = prog_b.calc(input_data)
        self.assertEqual(1, output_data)

        input_data = 5000
        output_data = prog_b.calc(input_data)
        self.assertEqual(50, output_data)

    def test_03(self):
        """ test 3
        6km 以上 30km 以下：
          距離 (km) に 50 を足した値とする。
        """
        input_data = 6000
        output_data = prog_b.calc(input_data)
        self.assertEqual(56, output_data)

        input_data = 30000
        output_data = prog_b.calc(input_data)
        self.assertEqual(80, output_data)

    def test_04(self):
        """ test 4
        35km 以上 70km 以下：
          距離 (km) から 30 を引いて 5 で割った後、80 を足した値とする。
        """
        input_data = 35000
        output_data = prog_b.calc(input_data)
        self.assertEqual(81, output_data)

        input_data = 70000
        output_data = prog_b.calc(input_data)
        self.assertEqual(88, output_data)

    def test_05(self):
        """ test 5
        70km より大きい：
          VVの値は 89 とする。
        """
        input_data = 70001
        output_data = prog_b.calc(input_data)
        self.assertEqual(89, output_data)


if __name__ == "__main__":
    unittest.main()

# EOF
