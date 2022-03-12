from datetime import datetime
import locale
import sys
import unittest

sys.path.append("..")


from src.time_skill import Time_Skill


class Time_Skill_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.ts = Time_Skill()

    def test_if_locale_was_set_to_default_in_init(self):
        # 0 index provide country code
        self.assertIn(locale.getdefaultlocale()[0], self.ts._locale)

    def test_if_datetime_was_called_in_init(self):
        self.assertEqual(self.ts._today.date(), datetime.today().date())

    def test_get_date_is_str_type(self):
        self.assertTrue(type(self.ts.get_date()) is str)

    def test_get_week_number_is_str_type(self):
        self.assertTrue(type(self.ts.get_week_number()) is str)

    def test_get_time_is_str_type(self):
        self.assertTrue(type(self.ts.get_time()) is str)


if __name__ == "__main__":
    unittest.main()
