import sys
import unittest

sys.path.append("..")

from src.weather_skill import Weather_Skill


class Weather_Skill_Test(unittest.TestCase):
    def test_city_name_gdansk_if_no_city_in_init(self):
        self.ws = Weather_Skill()
        self.assertEqual(self.ws.city, "Gdańsk")

    def test_city_namr_equal_to_provided(self):
        self.ws = Weather_Skill(city="Warszawa")
        self.assertEqual(self.ws.city, "Warszawa")


if __name__ == "__main__":
    unittest.main()
