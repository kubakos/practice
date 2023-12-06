#!/usr/bin/env python3
import honeycomb


def input_data(test_case):
    f = open('sample-data/' + str(test_case) + '.in', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    row1 = [int(i) for i in data[0].split(' ')]
    row2 = [int(i) for i in data[1].split(' ')]
    return row1, row2


if __name__ == '__main__':
    x = honeycomb.Honeycomb(input_data(1))
    step_count = x.get_path()
    print(step_count)
