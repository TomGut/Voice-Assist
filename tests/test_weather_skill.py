import sys
import unittest

sys.path.append("..")

from src.weather_skill import WeatherSkill


class WeatherSkillTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ws = WeatherSkill()

    def test_city_name_gdansk_if_no_city_in_init(self):
        self.assertEqual(self.ws.city, "Gdańsk")

    def test_if_temp_return_string(self):
        self.assertIsInstance(self.ws.temp(), str)


if __name__ == "__main__":
    unittest.main()
