#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import numpy as np

class Map:
    def __init__(self, sx, sy, weight):
        self.x = sx
        self.y = sy
        self.w = weight
        self.patients_distances = None
        self.hub_distances = None

    def set_hub(self, hub):
        self.hub = hub

    def set_patients(self, patients):
        self.patients = patients

    def patients_count(self):
        return len(self.patients)


def init_distances(world: Map):
    size = world.patients_count()
    return np.zeros((size, size))


def distance(a, b):
    tmp = map(lambda x: (x[0] - x[1])**2,  zip(a, b))
    return np.sqrt(sum(tmp))


def build_patients_distances(world: Map):
    out = init_distances(world)
    for i, start in enumerate(world.patients):
        for j, dest in enumerate(world.patients):
            if j >= i:
                out[j][i] = out[i][j] = distance(start, dest)

    return world.w * out


def build_hub_distances(world: Map):
    out = [world.w * distance(world.hub, p) for p in world.patients]
    return out


def build_distances(world: Map):
    pat_dist = build_patients_distances(world)
    hub_dist = build_hub_distances(world)
    world.patients_distances = pat_dist
    world.hub_distances = hub_dist
