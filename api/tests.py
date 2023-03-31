import unittest
from api.services.analytics_services import GraduationAttendanceMissingDays


class TestCaseOfGraduationCeremony(unittest.TestCase):
    # Test cases been written on the output suggested in the question
    def test_calculate_attendance_and_missing(self):
        obj = GraduationAttendanceMissingDays()
        self.assertEqual(obj.calculate_attendance_and_missing(5), "14/29")
        self.assertEqual(obj.calculate_attendance_and_missing(10), "372/773")


if __name__ == '__main__':
    unittest.main()
