#!/usr/bin/env python3
import army


def input_data():
    f = open('sample-data/1.in', 'r')
    tmp = f.read()
    f.close()
    tmp = [[i] for i in tmp.split('\n')]
    data = []
    for i in tmp:
        data.append([j for j in i[0].split(' ') if j != ''])
    return data


if __name__ == '__main__':
    x = army.Army(input_data())
