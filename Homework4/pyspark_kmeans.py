from pyspark import SparkContext
import numpy as np


def distance(p, centroids):
    dist = []
    for c in centroids:
        dist.append(np.linalg.norm(p - c))
    return dist


def pyspark_kmeans(data_file, centroid_file, max_iter=100):
    """

    :param data_file: the txt file contains the data points
    :param centroid_file: the txt file contains the starting centroids
    :param max_iter: maximum times of iteration; default value is 100
    :return: txt file (centroid.txt) contains the ending centroids
    """
    sc = SparkContext('local[2]', 'pyspark kmeans')
    data = sc.textFile(data_file).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    centroids_new = sc.textFile(centroid_file).map(lambda line: np.array([float(x) for x in line.split(' ')]))

    for _ in range(max_iter):
        centroids_old = centroids_new.collect()
        cluster = data.map(lambda l: (l, distance(l, centroids_old)))
        cluster_id = cluster.map(lambda l: (np.argmin(l[1]), l[0]))

        cluster_sum = cluster_id.reduceByKey(lambda n1, n2: np.add(n1, n2))
        count = cluster.map(lambda l: (np.argmin(l[1]), 1)).reduceByKey(lambda n1, n2: n1 + n2)
        centroids_new = cluster_sum.join(count).map(lambda l: l[1][0] / float(l[1][1]))

    output = centroids_new.collect()
    np.savetxt('centroid.txt', output)


if __name__ == "__main__":
    pyspark_kmeans('data.txt', 'c1.txt')
