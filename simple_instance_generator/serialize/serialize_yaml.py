#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import yaml
from .instance_store import InstanceStore

class SerializeYaml(InstanceStore):
    def __init__(self):
        super(SerializeYaml, self).__init__()

    def serialize(self):
        return yaml.safe_dump(self.store)

