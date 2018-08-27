import numpy as np
class Graph(object):
    def __init__(self):
        pass

    def neighbor(self, graph, node):
        """
        Return a list of neighbor nodes
        :param graph: dictionary, the output of read_file
        :param node: string
        :return: list of string
        """
        neighbor = [i for i, j in graph[node]]
        return neighbor

    def weight(self, graph, node1, node2):
        """
        Return the weight of the edge connecting node1 and node2;
        If node1 and node2 are disconnected, return inf.
        :param graph: dictionary
        :param node1: string
        :param node2: string
        :return: double or inf
        """
        if node2 in self.neighbor(graph, node1):
            for i, j in graph[node1]:
                if i == node2:
                    w = j
        else:
            w = np.inf
        return w

    def read_file(self, name_txt_file):
        """

        :param name_txt_file: txt file
        :return: dictionary, key: node, value: (neighbor node, weight)
        """
        with open(name_txt_file, "r") as f:
            graph = {}
            line_id = 0
            for i in f:
                i = i.replace('\n', '')
                if line_id % 2 == 0:
                    new_key = int(i)
                    graph[new_key] = []
                elif i != '' and i[0] == '(' and line_id % 2 == 1:
                    graph[new_key] = eval('[' + i.replace('\n', '') + ']')
                    graph[new_key] = [(i[0], i[1]) for i in graph[new_key]]
                else:
                    pass
                line_id = line_id + 1
        return graph

    def find_negative_circles(self, name_txt_file):
        """
        Use Bellman Ford algorithm to find negative circle
        :param name_txt_file: txt file
        :return: list of the str. e.g. if graph has circle 5-6-7-5, return ['5','6','7']
        """
        graph = self.read_file(name_txt_file)
        num_node = len(graph.keys())
        for t in graph.keys():
            F = {}
            path = {}
            for node in graph.keys():
                if node == t:
                    for k in range(num_node + 1):
                        F[(k, node)] = 0
                else:
                    F[(0, node)] = np.inf

            for n in range(1, num_node + 1):
                for s in graph.keys():
                    if s != t:
                        min_F = F[(n - 1, s)]
                        for v in self.neighbor(graph, s):
                            if F[(n - 1, v)] + self.weight(graph, s, v) < min_F:
                                min_F = F[(n - 1, v)] + self.weight(graph, s, v)
                                next_node = v
                        F[(n, s)] = min_F
                        if F[(n, s)] < F[(n - 1, s)]:
                            path[s] = next_node
            for s in graph.keys():
                if F[(num_node, s)] < F[(num_node - 1, s)]:  # graph has negative circle
                    neg_circle = True
                    l = [s]
                    next_node = path[s]
                    while next_node not in l:
                        l.append(next_node)
                        next_node = path[next_node]
                    circle = l[l.index(next_node):]
                    circle.append(next_node)
                    return circle
        return None
