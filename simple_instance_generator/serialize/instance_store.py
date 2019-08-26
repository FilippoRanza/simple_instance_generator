#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from .translate import Translate
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


    def __init__(self, translate_file, serializer: Serializer):
        self.serializer = serializer
        self.store = {}
        self.patients = None
        self.requests = None
        self.translate = Translate(translate_file)

    def set_nurse_work_time(self, time):
        self._store_value_(InstanceStore.NURSES_WORK_TIME, time)

    def set_nurses(self, nurses):
        self._store_value_(InstanceStore.NURSES, nurses)


    def set_world_map(self, world_map):
        self._store_value_(InstanceStore.HUB, world_map.hub)
        self._store_value_(InstanceStore.HUB_DISTANCE, world_map.hub_distances)
        self._store_value_(InstanceStore.PATIENTS_DISTANCE, world_map.patients_distances.tolist())
        self.patients = world_map.patients
        self._generate_users_()

    def set_services(self, services):
        self._store_value_(InstanceStore.SERVICES, services)

    def set_requests(self, requests):
        self.requests = requests.T
        self._generate_users_()

    def serialize(self):
        return self.serializer.serialize(self.store, self.translate)

    def _generate_users_(self):
        id_name = self.translate.get_name(InstanceStore.ID)
        request_name = self.translate.get_name(InstanceStore.REQUEST)
        if self.patients and (self.requests is not None) :
            tmp = [{id_name: p, request_name: r.tolist()} for p, r in zip(self.patients, self.requests)]
            self._store_value_(InstanceStore.PATIENTS, tmp)

    def _store_value_(self, key, value):
        key = self.translate.get_name(key)
        self.store[key] = value
