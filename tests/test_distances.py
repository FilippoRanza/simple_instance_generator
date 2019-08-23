#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest

from simple_instance_generator.map import distance, build_distances, Map


class TestDistances(unittest.TestCase):
    
    def test_known_ans(self):
        self.assertEqual(distance((0, 0), (0, 3)), 3)
        self.assertEqual(distance((4, 5), (4, 5)), 0)
        self.assertEqual(distance((0, 3), (4, 6)), 5)
        
    def test_simmetry(self):
        self.assertEqual(distance((4, 5), (7, -8)), distance((7, -8), (4, 5)))
        self.assertEqual(distance((-4, 1.4), (-7.8, 4)), distance((-7.8, 4), (-4, 1.4)))


class TestBuildDistances(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBuildDistances, self).__init__(*args, **kwargs)
        self.world = Map(100, 100, 1)
        self.world.set_hub((10, 10))
        self.world.set_patients([(5, 6), (14, 5), (6, 89), (87, 41)])
        build_distances(self.world)

    def test_zero_diagonal(self):
        dist = self.world.patients_distances
        for i, row in enumerate(dist):
            for j, value in enumerate(row):
                if i == j:
                    self.assertEqual(value, 0)


    def test_simmetry(self):
        dist = self.world.patients_distances
        size = self.world.patients_count()
        for i in range(size):
            for j in range(size):
                self.assertEqual(dist[i][j], dist[j][i])


if __name__ == "__main__":
    unittest.main()
