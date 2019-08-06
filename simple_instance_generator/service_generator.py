#! /usr/bin/python3

from secrets import randbelow


class ServiceContainer:
    def __init__(self, slot_size):
        self.sz = slot_size

    def set_services(self, service):
        self.service = service
    

def make_service(tmin, tmax):
    return randbelow(tmax - tmin + 1) + tmin

def service_generator(tmin, tmax, slot_size, service_count):
    services = [make_service(tmin, tmax) for _ in range(service_count)]
    out = ServiceContainer(slot_size)
    out.set_services(services)
    return out