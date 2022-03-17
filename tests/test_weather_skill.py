import sys
import unittest
from unittest.mock import patch

sys.path.append("..")

from src.weather_skill import Weather_Skill


class Weather_Skill_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ws = Weather_Skill()

    def test_city_name_gdansk_if_no_city_in_init(self):
        self.assertEqual(self.ws.city, "Gdańsk")

    def test_if_temp_return_string(self):
        self.assertIsInstance(self.ws.temp(), str)


if __name__ == "__main__":
    unittest.main()
