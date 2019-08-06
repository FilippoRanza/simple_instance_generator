#! /usr/bin/python3

import unittest
from secrets import randbelow

from simple_instance_generator.map import Map
from simple_instance_generator.map_generator import map_generator

RAND_MAX = 150
RAND_MIN = 10

PATIENTS_MAX = 30

SX = randbelow(RAND_MAX - RAND_MIN) + RAND_MIN
SY = randbelow(RAND_MAX - RAND_MIN) + RAND_MIN
PATIENTS = randbelow(PATIENTS_MAX - RAND_MIN) + RAND_MIN


class TestMapGenerator(unittest.TestCase):

    def test_base(self):
        map_obj = map_generator(SX, SY, PATIENTS, True, 1)
        self.assertIsInstance(map_obj, Map)

    def test_values(self):
        map_obj = map_generator(SX, SY, PATIENTS, True, 1)
        patients = map_obj.patients
        self.assertIsInstance(patients, set)
        self.assertEqual(len(patients), PATIENTS)
        self.assertEqual(map_obj.y, SY)
        self.assertEqual(map_obj.y, SY)
        self.assertEqual(map_obj.patients_count(), PATIENTS)

    def test_size_error(self):
        try:
            max_count = (SX * SY) - 1
            map_generator(SX, SY, max_count, True, 1)
        except ValueError:
            self.fail('should not raise error here')

        min_error_count = (SX * SY)
        self.assertRaises(ValueError, map_generator, SX, SY, min_error_count, True, 1)

        error_count = min_error_count * 3
        self.assertRaises(ValueError, map_generator, SX, SY, error_count, True, 1)



if __name__ == "__main__":
    unittest.main()
