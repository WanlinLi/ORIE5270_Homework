import unittest
from multiply_folder.multiplication import multiplication

class testmultiple(unittest.TestCase):
    def test1(self):
        M = multiplication()
        self.multi1 = M.spark_multiplication('./A1.txt', './B1.txt')
	self.multi1 = self.multi1.collect()
        self.answer1 = [68, 167]
        assert self.multi1 == self.answer1

    def test2(self):
        M = multiplication()
        self.multi2 = M.spark_multiplication('A2.txt', 'B2.txt').collect()
        self.answer2 = [3535, 193, 536, -3782]
        assert self.multi2 == self.answer2
