import unittest
from find_path_folder.find_path import Graph


class testcircle(unittest.TestCase):
    def test_tree(self):
        path = "/home/wanlinli/ORIE5270_Homework/Homework3/dijkstra_folder/test_folder/"
        graph = Graph()
        self.dist1 = graph.find_shortest_path(path + 'test1.txt', '1', '8')
        self.answer1 = 14
        assert self.dist1 == self.answer1

    def test_graph1(self):
        path = "/home/wanlinli/ORIE5270_Homework/Homework3/dijkstra_folder/test_folder/"
        graph = Graph()
        self.dist2 = graph.find_shortest_path(path + 'test2.txt', '1', '8')
        self.answer2 = 10
        assert self.dist2 == self.answer2

    def test_graph2(self):
        path = "/home/wanlinli/ORIE5270_Homework/Homework3/dijkstra_folder/test_folder/"
        graph = Graph()
        self.dist3 = graph.find_shortest_path(path + 'test2.txt', '4', '8')
        self.answer3 = 8
        assert self.dist3 == self.answer3
