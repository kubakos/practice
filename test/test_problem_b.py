#! /usr/bin/python3
import unittest
from problems.b.problem_b import *


class TestB(unittest.TestCase):

    def test_problem_b(self):
        a = open('problems/b/sample-data/1.ans', 'r')
        answer = a.read()
        a.close()
        hc = Honeycomb(input_data())
        self.assertEqual(hc.search(), answer)

        a = open('problems/b/sample-data/2.ans', 'r')
        answer = a.read()
        a.close()
        hc = Honeycomb(input_data())
        self.assertEqual(hc.search(), answer)


if __name__ == '__main__':
    unittest.main()
