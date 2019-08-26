#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import json
from .serializer import Serializer

class SerializeJson(Serializer):
    def serialize(self, store):
        return json.dumps(store)

