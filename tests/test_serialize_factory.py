#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest
from simple_instance_generator import serialize_factory
from simple_instance_generator.serialize.serialize_json import SerializeJson
from simple_instance_generator.serialize.serialize_text import SerializeText


class TestSerializeFactory(unittest.TestCase):

    def test_success(self):
        self.assertIsInstance(serialize_factory('text').serializer, SerializeText)
        self.assertIsInstance(serialize_factory('json').serializer, SerializeJson)


    def test_error(self):
        for wrong in ['something', 'toxt', 'jsons']:
            with self.assertRaisesRegex(ValueError, f'Unknown serializer {wrong}'):
                serialize_factory(wrong)


if __name__ == "__main__":
   unittest.main()
