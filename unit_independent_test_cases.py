import unittest
from independent_script import independent_calculate_attendance_and_missing


class TestCaseOfGraduationCeremony(unittest.TestCase):
    # Test cases been written on the output suggested in the question
    def test_calculate_attendance_and_missing(self):
        self.assertEqual(independent_calculate_attendance_and_missing(5), "14/29")
        self.assertEqual(independent_calculate_attendance_and_missing(10), "372/773")


if __name__ == '__main__':
    unittest.main()