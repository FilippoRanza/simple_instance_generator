#! /usr/bin/python3

import unittest

from simple_instance_generator.container_wrapper import ContainerWrapper


class TestContainerWrapper(unittest.TestCase):

    def test_unique(self):
        container = ContainerWrapper(True)
        self.assertIsInstance(container.data, set)
        try:
            for i in range(10):
                container.insert(i)

            for i in range(10):
                container.insert(i)
        except AttributeError:
            self.fail('this should be a set...')
        
        self.assertEqual(len(container.data), 10)
        
    def test_non_unique(self):
        container = ContainerWrapper(False)
        self.assertIsInstance(container.data, list)
        try:
            for i in range(10):
                container.insert(i)

            for i in range(10):
                container.insert(i)
        except AttributeError:
            self.fail('this should be a list...')
        
        self.assertEqual(len(container.data), 20)


if __name__ == "__main__":
    unittest.main()
