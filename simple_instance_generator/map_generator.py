#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from secrets import randbelow

from .map import Map, build_distances
from .container_wrapper import container_factory

class MapGenerator:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.hub = None

    def generate(self, sx, sy, patients, weight, unique=True):
        MapGenerator._check_size_(sx, sy, patients)
        self._setup_(sx, sy)
        pats = self._gen_patients_(patients, unique)
        out = Map(sx, sy, weight)
        out.set_hub(self.hub)
        out.set_patients(pats)
        return out


    @staticmethod
    def _check_size_(sx, sy, patients):
        places = (sx * sy) - 1
        if patients > places:
            raise ValueError(f"Map {sx}x{sy}: not enough space for {patients}")

    def _setup_(self, x, y):
        self.x = x
        self.y = y
        self.hub = self._rand_point_()

    def _rand_point_(self):
        x = randbelow(self.x)
        y = randbelow(self.y)
        return x, y

    def _gen_patients_(self, count, unique):
        out = container_factory(unique)
        while len(out) < count:
            tmp = self._rand_point_()
            if tmp != self.hub:
                out.insert(tmp)
        return out.get_collection()


def map_generator(size_x, size_y, patient_count, unique, weight):
    gen = MapGenerator()
    world = gen.generate(size_x, size_y, patient_count, weight, unique)
    build_distances(world)
    return  world
