#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from .serializer import Serializer


class InstanceStore:

    NURSES_WORK_TIME = 'NURSES_WORK_TIME'
    NURSES = 'NURSES'
    HUB = 'HUB'
    SERVICES = 'SERVICES'
    ID = 'ID'
    REQUEST = 'REQUEST'
    PATIENTS = 'PATIENTS'
    HUB_DISTANCE = 'HUB_DISTANCE'
    PATIENTS_DISTANCE = 'PATIENTS_DISTANCE'
    MAP_SIZE_X = 'MAP_SIZE_X'
    MAP_SIZE_Y = 'MAP_SIZE_Y'
    BASE_TIME_SLOT = 'BASE_TIME_SLOT'



    def __init__(self, serializer: Serializer):
        self.serializer = serializer
        self.store = {}
        self.patients = None
        self.requests = None

    def set_nurse_work_time(self, time):
        self.store[InstanceStore.NURSES_WORK_TIME] = time

    def set_nurses(self, nurses):
        self.store[InstanceStore.NURSES] = nurses


    def set_world_map(self, world_map):
        self.store[InstanceStore.HUB] = world_map.hub
        self.store[InstanceStore.HUB_DISTANCE] = world_map.hub_distances
        self.store[InstanceStore.PATIENTS_DISTANCE] = world_map.patients_distances.tolist()
        self.patients = world_map.patients
        self._generate_users_()

    def set_services(self, services):
        self.store[InstanceStore.SERVICES] = services

    def set_requests(self, requests):
        self.requests = requests.T
        self._generate_users_()

    def set_map_size(self, sizex, sizey):
        self.store[InstanceStore.MAP_SIZE_X] = sizex
        self.store[InstanceStore.MAP_SIZE_Y] = sizey

    def set_base_time_slot(self, time_slot):
        self.store[InstanceStore.BASE_TIME_SLOT] = time_slot

    def serialize(self):
        return self.serializer.serialize(self.store)

    def _generate_users_(self):
        if self.patients and (self.requests is not None) :
            tmp = [{InstanceStore.ID : p, InstanceStore.REQUEST: r.tolist()}
                    for p, r in zip(self.patients, self.requests)]
            self.store[InstanceStore.PATIENTS]= tmp


