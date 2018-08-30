import unittest
from multiply_folder.multiplication import multiplication


class testmultiple(unittest.TestCase):
    def test1(self):
        M = multiplication()
        self.multi1, sc = M.spark_multiplication('./test_folder/A1.txt', './test_folder/B1.txt')
        self.multi1 = self.multi1.collect()
        sc.stop()
        self.answer1 = [68, 167]
        assert self.multi1 == self.answer1

    def test2(self):
        M = multiplication()
        self.multi2, sc = M.spark_multiplication('./test_folder/A2.txt', './test_folder/B2.txt')
        self.multi2 = self.multi2.collect()
        sc.stop()
        self.answer2 = [3535, 193, 536, -3782]
        assert self.multi2 == self.answer2

