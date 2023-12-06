
class Honeycomb:

    def __init__(self, data):
        self.edge_length = data[0][0]
        self.mid_length = 2 * self.edge_length - 1
        self.total_cell_count = self.edge_length**3 - (self.edge_length - 1)**3
        self.hardened_cell_count = data[0][4]
        self.hardened_cell_id = data[1]
        self.hardened_cell_loc = []
        self.max_step = data[0][1]
        self.starting_node = None
        self.end_node = None
        self.graph = self.generate_graph_keys()
        for key in self.graph:
            self.graph[key] = self.find_edges(key)
        for i, key in enumerate(self.graph):
            if i + 1 == data[0][2]:
                self.starting_node = key
            elif i + 1 == data[0][3]:
                self.end_node = key
        for i, key in enumerate(self.graph):
            if i + 1 in self.hardened_cell_id:
                self.hardened_cell_loc.append(key)
        self.node_weights = self.generate_heuristic_map()
        self.path = self.astar(self.starting_node, self.end_node)

    def get_path(self):
        if isinstance(self.path, list):
            if len(self.path) - 1 <= self.max_step:
                return len(self.path) - 1
            else:
                return 'No'
        else:
            return self.path

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
        for row in range(-1, 2):
            for col in range(-1, 2):
                if key[0] < self.edge_length - 1:
                    if ((row > 0) & (col < 0)) or ((row < 0) & (col > 0)) or ((row == 0) & (col == 0)):
                        continue
                    if (key[0] + row, key[1] + col) in self.graph.keys():
                        edges.append([key[0] + row, key[1] + col])
                elif key[0] == self.edge_length - 1:
                    if ((row > 0) & (col > 0)) or ((row < 0) & (col > 0)) or ((row == 0) & (col == 0)):
                        continue
                    if (key[0] + row, key[1] + col) in self.graph.keys():
                        edges.append([key[0] + row, key[1] + col])
                elif key[0] > self.edge_length - 1:
                    if ((row > 0) & (col > 0)) or ((row < 0) & (col < 0)) or ((row == 0) & (col == 0)):
                        continue
                    if (key[0] + row, key[1] + col) in self.graph.keys():
                        edges.append([key[0] + row, key[1] + col])
        return edges

    def generate_heuristic_map(self):
        h = {}
        h[self.end_node] = 0
        weight = 0
        wax_hardened_cell_weight = float('inf')
        frontier = self.graph.copy()
        neighbours = [frontier.pop(self.end_node)]

        while len(frontier) > 0:
            weight += 1
            next_order_neighbours = []

            for neighbour in neighbours:
                for i in neighbour:
                    i = (i[0], i[1])
                    if (i in self.hardened_cell_loc) & (i in frontier):
                        h[i] = wax_hardened_cell_weight
                        next_order_neighbours.append(
                            frontier.pop(i))
                        continue
                    elif i in frontier:
                        h[i] = weight
                        next_order_neighbours.append(
                            frontier.pop(i))

            neighbours = next_order_neighbours
        return h

    def astar(self, path_start, path_end):
        # nodes that have uninspected neighbour(s)
        nodes_to_inspect = set([path_start])
        # all neighbours of nodes have been inspected
        inspected_nodes = set([])

        # contains travel costs from path_start to registered nodes - g()
        travel_cost = {}
        travel_cost[path_start] = 0

        # contains the registered paths from path_start
        parent_node = {}
        parent_node[path_start] = path_start

        while len(nodes_to_inspect) > 0:
            current_node = None

            # find a node with the lowest value of f()
            for n in nodes_to_inspect:
                if current_node == None or travel_cost[n] + self.node_weights[n] < travel_cost[current_node] + self.node_weights[current_node]:
                    current_node = (n[0], n[1])

            # if end of path node reached, return the path
            if current_node == path_end:
                path = []

                while parent_node[current_node] != current_node:
                    path.append(current_node)
                    current_node = parent_node[current_node]

                path.append(path_start)
                path.reverse()

                return path

            # for all neighbors of the current node do
            for neighbour in self.graph[current_node]:
                neighbour = (neighbour[0], neighbour[1])
                if neighbour not in nodes_to_inspect and neighbour not in inspected_nodes:
                    if self.node_weights[neighbour] != float('inf'):
                        nodes_to_inspect.add(neighbour)
                        parent_node[neighbour] = current_node
                        travel_cost[neighbour] = travel_cost[current_node] + \
                            self.node_weights[current_node]
                else:
                    if travel_cost[neighbour] > travel_cost[current_node] + self.node_weights[current_node]:
                        parent_node[neighbour] = current_node
                        travel_cost[neighbour] = travel_cost[current_node] + \
                            self.node_weights[current_node]

                        if neighbour in inspected_nodes:
                            inspected_nodes.remove(neighbour)
                            nodes_to_inspect.add(neighbour)

            nodes_to_inspect.remove(current_node)
            inspected_nodes.add(current_node)

        return 'Path does not exist!'
