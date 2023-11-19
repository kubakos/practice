#!/usr/bin/env python3
import honeycomb


def input_data():
    f = open('sample-data/1.in', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    row1 = [int(i) for i in data[0].split(' ')]
    row2 = [int(i) for i in data[1].split(' ')]
    return row1, row2


if __name__ == '__main__':
    print(input_data())
    x = honeycomb.Honeycomb(input_data())
    print(x.get_graph())
