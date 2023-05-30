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
from queue import PriorityQueue


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

    def astar(self):
        # Set up initial values
        frontier = PriorityQueue()
        frontier.put(self.starting_point, 0)
        came_from = {}
        cost_so_far = {}
        came_from[self.starting_point] = None
        cost_so_far[self.starting_point] = 0

        # Loop until the goal is reached or the frontier is empty
        while not frontier.empty():
            # Get the node with the lowest cost from the frontier
            current_node = frontier.get()

            # Check if the goal has been reached
            if current_node == self.end_point:
                break

            # Loop through the node's neighbors
            for neighbor_node, cost in current_node.neighbors():
                # Calculate the total cost of reaching the neighbor node
                new_cost = cost_so_far[current_node] + cost

                # Check if the neighbor node has not been visited before or if a better path to it has been found
                if neighbor_node not in cost_so_far or new_cost < cost_so_far[neighbor_node]:
                    # Update the cost and priority of the neighbor node
                    cost_so_far[neighbor_node] = new_cost
                    priority = new_cost + \
                        self.heuristic(self.end_point, neighbor_node)
                    frontier.put(neighbor_node, priority)
                    came_from[neighbor_node] = current_node

        return came_from, cost_so_far

    def heuristic(self, goal_node, neighbor_node):
        # Calculate the heuristic value between the neighbor node and the goal node
        return abs(goal_node.x - neighbor_node.x) + abs(goal_node.y - neighbor_node.y)
