#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from .serialize_json import SerializeJson
from .serialize_yaml import SerializeYaml
from .serialize_text import SerializeText

SERIALIZERS = {
    'json': SerializeJson,
    'yaml': SerializeYaml,
    'text': SerializeText
}


def generate_error(name):
    msg = f'Unknown serializer {name}\n Known serializers:\n'
    msg += '\n'.join(SERIALIZERS.keys())
    raise ValueError(msg)


def serialize_factory(serialization_name):
    serializer = SERIALIZERS.get(serialization_name)
    if serializer is None:
        generate_error(serialization_name)
    return serializer()
