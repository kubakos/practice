#! /usr/bin/python3
import unittest
from problems.b.problem_b import *


class TestB(unittest.TestCase):

    def test_honeycomb_graph_keys(self):
        print(Honeycomb(input_data()).get_graph())


if __name__ == '__main__':
    unittest.main()
