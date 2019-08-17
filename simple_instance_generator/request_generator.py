#! usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from secrets import randbelow

import numpy
from .normal_rand_int import make_normal_random_int


class RequestGenerator:

    def __init__(self, patients, days, services, mean=0):
        self.mat = numpy.zeros((days, patients), dtype=numpy.uint16)
        self.patient_services = [randbelow(services) for _ in range(patients)]
        self.patient_count = patients
        if not mean:
            mean = self.patient_count // 2
        self.func = make_normal_random_int(mean, 1, self.patient_count)


    def generate(self):
        for v in self.mat:
            self._generate_day_(v)
        return self.mat


    def _generate_day_(self, day):
        request_count = self.func()
        patients = self._choose_patients_(request_count)
        for p in patients:
            # zero means no request
            day[p] = self.patient_services[p] + 1


    def _choose_patients_(self, count):
        out = set()
        while len(out) < count:
            tmp = randbelow(self.patient_count)
            out.add(tmp)
        return out


def request_generator(world_map, services, time_horizon, mean_request=0):
    gen = RequestGenerator(world_map.patients_count(),
                           time_horizon, services.service_count(), mean_request)
    return gen.generate()

