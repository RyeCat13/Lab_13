import unittest
import Grades

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, 'The total function should return 33')

    def test_total_returns_0(self):
        return 0

    def test_average_one(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, 3)

    def test_average_two(self):
        result = [2, 15, 22, 9]
        return 12.0000

    def test_average_returns_nan(self):
        with self.assertIs(average):
            return math.nan

    def test_median_one(self):
        result = [2, 5, 1]
        self.assertEqual(result, 2)

    def test_median_two(self):
        result = [5, 2, 1, 3]
        self.assertEqual(result, 2.5)
    
unittest.main()

