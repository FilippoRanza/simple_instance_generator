#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest

from simple_instance_generator.container_wrapper import container_factory


class TestContainerWrapper(unittest.TestCase):

    def test_unique(self):
        container = container_factory(True)
        self.assertIsInstance(container.get_collection(), set)
        try:
            for i in range(10):
                container.insert(i)

            for i in range(10):
                container.insert(i)
        except AttributeError:
            self.fail('this should be a set...')

        self.assertEqual(len(container), 10)

    def test_non_unique(self):
        container = container_factory(False)
        self.assertIsInstance(container.get_collection(), list)
        try:
            for i in range(10):
                container.insert(i)

            for i in range(10):
                container.insert(i)
        except AttributeError:
            self.fail('this should be a list...')

        self.assertEqual(len(container), 20)


if __name__ == "__main__":
    unittest.main()
