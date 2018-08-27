import heapq
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
        else:            w = np.inf
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
                    graph[new_key] = [((i[0]), i[1]) for i in graph[new_key]]
                else:
                    pass
                line_id = line_id + 1
        return graph

    def find_shortest_path(self, name_txt_file, source, destination):
        # use dijiktra,
        # return (int)
        graph = self.read_file(name_txt_file)
        vertex = graph.keys()
        dist = {}
        for v in vertex:
            if v == source:
                dist[v] = 0
            else:
                dist[v] = np.inf
        settlement = {}
        path = {}
        frontier = [(0, source)]
        while frontier:
            heapq.heapify(frontier)
            min_dist_frontier = heapq.heappop(frontier)
            min_dist = min_dist_frontier[0]
            min_dist_node = min_dist_frontier[1]
            settlement[min_dist_node] = min_dist

            for node in self.neighbor(graph, min_dist_node):
                if node not in settlement.keys():
                    heapq.heappush(frontier, (dist[node], node))

            for i in range(len(frontier)):
                d = frontier[i][0];
                v = frontier[i][1]
                if min_dist + self.weight(graph, min_dist_node, v) < d:
                    d = min_dist + self.weight(graph, min_dist_node, v)
                    dist[v] = d
                    frontier[i] = (d, v)
                    path[v] = min_dist_node
        short_path = [destination]; v = destination
        while v != source:
            short_path.append(path[v])
            v = path[v]
        short_path = short_path[::-1]
        return settlement[destination], short_path
