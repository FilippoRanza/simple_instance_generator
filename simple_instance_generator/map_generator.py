#! /usr/bin/python3

from secrets import randbelow

from .map import Map
from .container_wrapper import ContainerWrapper

class MapGenerator:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.hub = None

    def generate(self, sx, sy, patients, weight, unique=True):
        self._setup_(sx, sy)
        pats = self._gen_patients_(patients, unique)
        out = Map(sx, sy, weight)
        out.set_hub(self.hub)
        out.set_patients(pats)
        return out

    def _setup_(self, x, y):
        self.x = x
        self.y = y
        self.hub = self._rand_point_()

    def _rand_point_(self):
        x = randbelow(self.x)
        y = randbelow(self.y)
        return x, y

    def _gen_patients_(self, count, unique):
        out = ContainerWrapper(unique)
        while len(out) < count:
            tmp = self._rand_point_()
            if tmp != hub:
                out.insert(tmp)
        return out.data


def map_generator(size_x, size_y, patient_count, unique, weight):
    gen = MapGenerator()
    return gen.generate(size_x, size_y, patient_count, weight, unique)
