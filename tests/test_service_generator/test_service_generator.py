#! /usr/bin/python3

import unittest
from secrets import randbelow

from simple_instance_generator.service_generator import *

RANDMAX = 150
RANDMIN = 1

def make_times(rmin, rmax):
    a = randbelow(rmax - rmin) + rmin
    b = randbelow(rmax - rmin) + rmin
    # max + 1 ensures that there is always a delta
    # this value never goes over RANDMAX due to
    # randbelow properties
    if a < b:
        return a, (b + 1)
    return b, (a + 1)



class TestServiceGenerator(unittest.TestCase):

    def test_make_service(self):
        tmin, tmax = make_times(RANDMIN, RANDMAX)
        delta = tmax - tmin
        # set min to the possible maximum, and viceversa
        v_min = RANDMAX
        v_max = RANDMIN
        # repeat 10 times the number of possible values
        # just to be sure to find all possible values
        for _ in range(10 * delta):
            v = make_service(tmin, tmax)
            if v > v_max:
                v_max = v
            elif v < v_min:
                v_min = v

        self.assertEqual(v_max, tmax)
        self.assertEqual(v_min, tmin)


    def test_service_generator(self):
        tmin, tmax = make_times(RANDMIN, RANDMAX)
        count = randbelow(RANDMAX - RANDMIN) + RANDMIN
        # 15 is just a random number, it doesn't metter here
        service = service_generator(tmin, tmax, 15, count)

        self.assertIsInstance(service, ServiceContainer)

        services = service.service
        self.assertEqual(len(services), count)
        self.assertLessEqual(max(services), tmax)
        self.assertGreaterEqual(min(services), tmin)

        self.assertEqual(service.service_count(), count)

if __name__ == "__main__":
    unittest.main()

