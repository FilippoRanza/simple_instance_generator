#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest
from simple_instance_generator import serialize_factory
from simple_instance_generator.serialize.serialize_json import SerializeJson
from simple_instance_generator.serialize.serialize_text import SerializeText
from simple_instance_generator.serialize.serialize_yaml import SerializeYaml

class TestSerializeFactory(unittest.TestCase):

    def test_success(self):
        self.assertIsInstance(serialize_factory('text', None), SerializeText)
        self.assertIsInstance(serialize_factory('json', None), SerializeJson)
        self.assertIsInstance(serialize_factory('yaml', None), SerializeYaml)


    def test_error(self):
        for wrong in ['something', 'toxt', 'jsons']:
            with self.assertRaisesRegex(ValueError, f'Unknown serializer {wrong}'):
                serialize_factory(wrong, None)


if __name__ == "__main__":
   unittest.main()
