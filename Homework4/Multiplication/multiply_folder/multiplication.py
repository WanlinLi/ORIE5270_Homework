from pyspark import SparkContext

class multiplication(object):
    def add_index_matrix(self, l):
        for j in range(len(l)):
            yield (l[j], j)

    def add_index_vector(self, l):
        for j in range(len(l)):
            yield (j, l[j])

    def spark_multiplication(self, matrix_file, vector_file):
        """

        :param matrix_file: the txt file which contains the matrix, the first element of each row is the index
        :param vector_file: the txt file which contains the vector
        :return: a rdd object which contains the multiplication result (a vector)
        """
        sc = SparkContext('local[2]', 'pyspark matrix mult')
        A = sc.textFile(matrix_file).map(eval)
        A = A.map(lambda l: (l[0], list(l[1:-1])))
        A = A.flatMapValues(self.add_index_matrix)
        A = A.map(lambda l: (l[1][1], (l[0], l[1][0])))

        a = sc.textFile(vector_file).map(eval)
        a = a.flatMap(self.add_index_vector)
        r = A.join(a)
        r = r.map(lambda l: (l[0], (l[1][0][0], l[1][1] * l[1][0][1])))
        r = r.map(lambda l: l[1])
        r = r.reduceByKey(lambda n1, n2: n1 + n2).map(lambda l: l[1])

        return r

if __name__ == "__main__":
    M = multiplication()
    x = M.spark_multiplication('../test_folder/A1.txt','../test_folder/B1.txt')
    print(x.collect())
