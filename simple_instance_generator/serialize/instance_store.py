#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

class InstanceStore:

    def __init__(self):
        self.store = {}
        self.patients = None
        self.requests = None

    def set_nurse_work_time(self, time):
        self.store['NURSER_WORK_TIME'] = time

    def set_nurses(self, nurses):
        self.store['NURSES'] = nurses
       
    def set_world_map(self, world_map):
        self.store['HUB'] = world_map.hub
        self.patients = world_map.patients
        self._generate_users_()

    def set_services(self, services):
        self.store['SERVICES'] = services

    def set_requests(self, requests):
        self.requests = requests.T
        self._generate_users_()

    def _generate_users_(self):
        if self.patients and (self.requests is not None) :
            tmp = [{'ID': p, 'REQUEST': r} for p, r in zip(self.patients, self.requests)]
            self.store['PATIENTS'] = tmp