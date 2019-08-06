#! usr/bin/python3

from secrets import randbelow

import numpy


class RequestGenerator:

    def __init__(self, patients, days, services):
        self.mat = numpy.zeros((days, patients), dtype=numpy.uint16)
        self.patient_services = [randbelow(services) for _ in range(patients)]
        self.patient_count = patients


    def generate(self):
        for v in self.mat:
            self._generate_day_(v)
        return self.mat


    def _generate_day_(self, day):
        request_count = randbelow(self.patient_count + 1)
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


def request_generator(world_map, services, time_horizon):
    gen = RequestGenerator(world_map.patient_count(), time_horizon, services.services_count())
    return gen.generate()

