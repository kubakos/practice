
class Honeycomb:

    def __init__(self, data):
        self.edge_length = data[0][0]
        self.mid_length = 2 * self.edge_length - 1
        self.total_cell_count = self.edge_length**3 - (self.edge_length - 1)**3
        self.hardened_cell_count = data[0][4]
        self.hardened_cell_id = data[1]
        self.max_step = data[0][1]
        self.starting_node = None
        self.end_node = None
        self.graph = self.generate_graph_keys()
        for key in self.graph.keys():
            self.graph[key] = self.find_edges(key)
        for i, key in enumerate(self.graph):
            if i + 1 == data[0][2]:
                self.starting_node = key
            elif i + 1 == data[0][3]:
                self.end_node = key
        self.node_weights = self.generate_heuristic_map()
        self.path = self.astar(self.starting_node, self.end_node)

    def get_graph(self):
        return self.graph

    def get_path(self):
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
        frontier = self.graph
        neighbours = [frontier.pop(self.end_node)]

        while len(frontier) > 0:
            weight += 1
            next_order_neighbours = []

            for neighbour in neighbours:
                for i in neighbour:
                    if (i[0], i[1]) in frontier:
                        h[(i[0], i[1])] = weight
                        next_order_neighbours.append(
                            frontier.pop((i[0], i[1])))

            neighbours = next_order_neighbours
        return h

    def astar(self, path_start, path_end):
        # nodes that have uninspected neighbour(s)
        nodes_to_inspect = set(path_start)
        # all neighbours of nodes have been inspected
        inspected_nodes = set()

        # contains travel costs from path_start to registered nodes - g()
        travel_cost = {}
        travel_cost[path_start] = 0

        # contains the registered paths from path_start
        path = {}
        path[path_start] = [path_start]

        while len(nodes_to_inspect) > 0:
            current_node = None

            # find a node with the lowest value of f()
            for n in nodes_to_inspect:
                if current_node == None or travel_cost[n] + self.node_weights[n] < travel_cost[current_node] + self.node_weights[current_node]:
                    current_node = n

            # if end of path node reached, return the path
            if current_node == path_end:
                pass

        # ------------------------------------------------------------------------
        """
        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start_node)

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path

        # for all neighbors of the current node do
        for (m, weight) in self.get_neighbors(n):
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and g data
            # and if the node was in the closed_list, move it to open_list
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_list.remove(n)
        closed_list.add(n)
        """
        # -------------------------------------------------------------------------------------

        print("Path doesn't exist!")
        return 'No'
