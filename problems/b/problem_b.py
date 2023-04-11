"""
Input
The input contains two lines. The first line contains five blank separated integers: R N A B X
R: the length (number of cells) of each edge of the grid, where 2≤R≤20. The total number of cells in the grid can be determined by taking a difference of cubes, R3-(R-1)3.
N: the maximum number of cells 0x67 can chew through, where 1≤N<R3-(R-1)3.
A: the starting cell ID, This cell is located on one of the grid edges: The cell has fewer than six neighbors.
B: the cell ID of the cell containing the honey, where 1≤B≤R3-(R-1)3.
X: the number of wax-hardened cells, where 0≤X<(R3-(R-1)3)-1.
The second line contains X integers separated by spaces, where each integer is the ID of a wax-hardened cell.
The ID's, A, B, and all the ID's on the second line, are distinct positive integers less than or equal to R3-(R-1)3.

Output
A single integer K if 0x67 reached the honey at cell B, where B is the Kth cell, otherwise the string No if it was impossible to reach the honey by chewing through N cells or less. 
"""
#! /usr/bin/python3


def input_data():
    f = open('problems/b/sample-data/1.in', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    row1 = [int(i) for i in data[0].split(' ')]
    row2 = [int(i) for i in data[1].split(' ')]
    return row1, row2


class Honeycomb():

    def __init__(self, data):
        self.edge_length = data[0][0]
        self.mid_length = 2 * self.edge_length - 1
        self.total_cell_count = self.edge_length**3 - (self.edge_length - 1)**3
        self.hardened_cell_count = data[0][4]
        self.hardened_cell_id = data[1]
        self.max_step = data[0][1]
        self.starting_point = data[0][2]
        self.end_point = data[0][3]
        self.graph = self.generate_graph_keys()
        for key in self.graph.keys():
            self.graph[key] = self.find_edges(key)

    def get_graph(self):
        return self.graph

    def generate_graph_keys(self):
        keys = {}
        for row in range(self.edge_length):
            for col in range(self.mid_length):
                if col < self.edge_length + row:
                    keys[row, col] = []
                else:
                    break

        x = 0
        for row in range(self.edge_length, self.mid_length):
            x += 1
            for col in range(self.mid_length):
                if col < self.mid_length - x:
                    keys[row, col] = []
                else:
                    break

        return keys

    def find_edges(self, key):
        edges = []

        if key[0] < self.edge_length - 1:
            if (key[0] - 1, key[1] - 1) in self.graph.keys():
                edges.append([key[0] - 1, key[1] - 1])

            if (key[0] + 1, key[1] + 1) in self.graph.keys():
                edges.append([key[0] + 1, key[1] + 1])

        elif key[0] == self.edge_length - 1:
            if (key[0] - 1, key[1] - 1) in self.graph.keys():
                edges.append([key[0] - 1, key[1] - 1])

            if (key[0] + 1, key[1] - 1) in self.graph.keys():
                edges.append([key[0] + 1, key[1] - 1])

        elif key[0] > self.edge_length - 1:
            if (key[0] - 1, key[1] + 1) in self.graph.keys():
                edges.append([key[0] - 1, key[1] + 1])

            if (key[0] + 1, key[1] - 1) in self.graph.keys():
                edges.append([key[0] + 1, key[1] - 1])

        if (key[0] - 1, key[1]) in self.graph.keys():
            edges.append([key[0] - 1, key[1]])

        if (key[0], key[1] - 1) in self.graph.keys():
            edges.append([key[0], key[1] - 1])

        if (key[0] + 1, key[1]) in self.graph.keys():
            edges.append([key[0] + 1, key[1]])

        if (key[0], key[1] + 1) in self.graph.keys():
            edges.append([key[0], key[1] + 1])

        return edges

    def a_star(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
      # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0

        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v

            if n == None:
                print('No')
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('No')
        return None

    def search(self):
        answer = self.a_star(self.starting_point, self.end_point)
