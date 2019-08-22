#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import tempfile
import unittest
from simple_instance_generator.serialize.instance_store import Translate

class TestTranslate(unittest.TestCase):

    def test_empy_config(self):
        translate = Translate(None)
        for key in ['FOO', 'BAR', 'BAZ']:
            self.assertEqual(translate.get_name(key), key)

    def test_full_config(self):
        with tempfile.NamedTemporaryFile() as temp:
            temp.write(b'FOO: test\nBAR: key\nUSELESS: stuff')
            temp.seek(0)
            translate = Translate(temp.name)
            for key, trans in [('FOO', 'test'), ('BAR', 'key'), ('BAZ', 'BAZ')]:
                self.assertEqual(translate.get_name(key), trans)


if __name__ == "__main__":
    unittest.main()
