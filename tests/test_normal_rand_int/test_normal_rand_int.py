#! /usr/bin/python3


import unittest
from secrets import randbelow
from simple_instance_generator.normal_rand_int import make_normal_random_int



class TestFunction(unittest.TestCase):

    def test_is_function(self):
        f = make_normal_random_int(5, 0, 10)
        self.assertTrue(callable(f))

    def test_function_output(self):
        f = make_normal_random_int(5, 0, 10)
        a = f()
        self.assertEqual(len(a), 1)
        size = randbelow(1000) + 500
        a = f(size)
        self.assertEqual(len(a), size)


class TestValues(unittest.TestCase):

    def init_count(self, mean, begin, end):
        f = make_normal_random_int(mean, begin, end)

        rnd = f(1000000)
        value_count = {}
        for i in range(end - begin + 1):
            value_count[i] = 0

        for i in rnd:
            value_count[i] += 1
        return value_count


    def test_value_range(self):
        mean = 5
        begin = 0
        end = 10

        f = make_normal_random_int(mean, begin, end)
        rnd = f(1000000)
        self.assertEqual(min(rnd), 0)
        self.assertEqual(max(rnd), end)

    def test_value_bell(self):
        mean = randbelow(5) + 5
        begin = 0
        end = 2 * mean
        value_count = self.init_count(mean, begin, end)

        for i in range(mean):
            self.assertGreaterEqual(value_count[i + 1], value_count[i])

        for i in range(mean, end):
            self.assertLessEqual(value_count[i + 1], value_count[i])
            

    def test_two_functions(self):
        mean_a = randbelow(5) + 4
        mean_b = randbelow(43) + 12
        value_count_a = self.init_count(mean_a, 0, 14)
        value_count_b = self.init_count(mean_b, 12, 89)

        max_index_a = max(value_count_a, key=value_count_a.get)
        self.assertEqual(max_index_a, mean_a)

        max_index_b = max(value_count_b, key=value_count_b.get)
        self.assertEqual(max_index_b, mean_b)

if __name__ == "__main__":
    unittest.main()
