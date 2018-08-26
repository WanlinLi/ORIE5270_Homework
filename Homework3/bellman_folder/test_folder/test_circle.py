import unittest
from find_circle_folder.find_circle import Graph


class test_circle(unittest.TestCase):
    def test_positive_circle(self):
        graph = Graph()
        path = '/home/wanlinli/ORIE5270_Homework/Homework3/bellman_folder/test_folder'
        self.circle1 = graph.find_negative_circles(path+'/test1.txt')
        self.answer1 = []
        assert self.circle1 == self.answer1

    def test_no_circle(self):
        graph = Graph()
        path = '/home/wanlinli/ORIE5270_Homework/Homework3/bellman_folder/test_folder'
        self.circle2 = graph.find_negative_circles(path+'/test2.txt')
        self.answer2 = []
        assert self.circle2 == self.answer2

    def test_neg_circle(self):
        graph = Graph()
        path = '/home/wanlinli/ORIE5270_Homework/Homework3/bellman_folder/test_folder'
        self.circle3 = graph.find_negative_circles(path+'/test3.txt')
        self.answer3 = [['5', '7', '6'], ['7', '6', '5'], ['6', '5', '7']]
        assert self.circle3 in self.answer3
