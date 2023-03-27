"""
Input
Input begins with a line containing an integer N (1≤N≤100). The next N lines each contain one estimated cost, which is an integer between 0 and 10100.

Output
For each estimated cost, output the number of digits required to represent it.
"""
#! /usr/bin/python3


def input_data(d):
    f = open('problems/a/sample-data/' + d + '.in', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    return data


def length(data_in):
    ans = ''
    for i in data_in:
        ans += str(len(i)) + '\n'
    return ans[2:-1]
