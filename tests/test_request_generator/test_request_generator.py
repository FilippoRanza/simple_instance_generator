#! /usr/bin/python3

import unittest
from secrets import randbelow

from simple_instance_generator.request_generator import RequestGenerator

MAX_PATIENTS = 150
MIN_PATIENTS = 15

MAX_SERVICES = 30
MIN_SERVICES = 5

MAX_DAYS = 30
MIN_DAYS = 5

PATIENTS = randbelow(MAX_PATIENTS - MIN_PATIENTS) + MIN_PATIENTS
SERVICES = randbelow(MAX_SERVICES - MIN_SERVICES) + MIN_SERVICES
DAYS = randbelow(MAX_DAYS - MIN_DAYS) + MIN_DAYS


class TestRequestGenerator(unittest.TestCase):

    def test_matrix(self):
        gen = RequestGenerator(PATIENTS, DAYS, SERVICES)
        mat = gen.generate()
        self.assertEqual(len(mat), DAYS)
        for day in mat:
            self.assertEqual(len(day), PATIENTS)
            s_min = min(day)
            self.assertGreaterEqual(s_min, 0)
            s_max = max(day)
            self.assertLessEqual(s_max, SERVICES)
         
      
if __name__ == "__main__":
    unittest.main()
