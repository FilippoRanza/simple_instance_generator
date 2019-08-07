#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

class Map:
    def __init__(self, sx, sy, weight):
        self.x = sx
        self.y = sy
        self.w = weight

    def set_hub(self, hub):
        self.hub = hub

    def set_patients(self, patients):
        self.patients = patients

    def patients_count(self):
        return len(self.patients)
