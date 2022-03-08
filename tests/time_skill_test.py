import sys
import unittest

sys.path.append("..")


from src.time_skill import Time_Skill


class Time_Skill_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ts = Time_Skill()

    def test_get_date_is_str_type(self):
        self.assertTrue(type(self.ts.get_date()) is str)

    def test_get_week_number_is_str_type(self):
        self.assertTrue(type(self.ts.get_week_number()) is str)

    def test_get_time_is_str_type(self):
        self.assertTrue(type(self.ts.get_time()) is str)


if __name__ == "__main__":
    unittest.main()
