from queue import PriorityQueue


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
        pass
