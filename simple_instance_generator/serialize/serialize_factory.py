#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from .serialize_json import SerializeJson
from .serialize_text import SerializeText
from .serialize_latex_table import SerializeLatexTable
from .instance_store import InstanceStore

SERIALIZERS = {
    'latex': SerializeLatexTable,
    'json': SerializeJson,
    'text': SerializeText
}

def available_serializers():
    return SERIALIZERS.keys()

def generate_error(name):
    msg = f'Unknown serializer {name}\n Known serializers:\n'
    msg += '\n'.join(SERIALIZERS.keys())
    raise ValueError(msg)


def serialize_factory(serialization_name):
    serializer = SERIALIZERS.get(serialization_name)
    if serializer is None:
        generate_error(serialization_name)

    tmp = serializer()
    return InstanceStore(tmp)
