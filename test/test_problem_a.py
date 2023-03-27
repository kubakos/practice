#! /usr/bin/python3
import unittest
from problems.a.problem_a import length, input_data


class TestA(unittest.TestCase):

    def test_problem(self):
        a = open('problems/a/sample-data/1.ans', 'r')
        answer = a.read()
        a.close()
        self.assertEqual(length(input_data(str(1))), answer)

        a = open('problems/a/sample-data/2.ans', 'r')
        answer = a.read()
        a.close()
        self.assertEqual(length(input_data(str(2))), answer)


if __name__ == '__main__':
    unittest.main()
