#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import json
from .instance_store import InstanceStore

class SerializeJson(InstanceStore):
    def __init__(self, translate_file):
        super(SerializeJson, self).__init__(translate_file)

    def serialize(self):
        return json.dumps(self.store)

