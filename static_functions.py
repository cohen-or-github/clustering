from sample import Sample


def minimum(x, y):
    """
    :param x: number
    :param y: number
    :return: the smallest number
    """
    if x < y:
        return x
    else:
        return y


def in_xy(sample, cluster):
    """
    :param sample: a sample
    :param cluster: the cluster to which the sample belongs
    :return: the in value
    """
    total = 0
    length = len(cluster.samples)
    in_x = 0
    for second_sample in cluster.samples:
        total += Sample.compute_euclidean_distance(sample, second_sample)
    in_x = (1 / (length - 1)) * total
    return in_x


def out_xy (clusters, curr_cluster, sample):
    """
    :param clusters: list of clusters
    :param curr_cluster: the samples's cluster
    :param sample: the curr sample
    :return: the out value
    """
    smallest = float('inf')
    curr_out = 0
    total = 0
    for cluster in clusters:
        if cluster == curr_cluster:
            continue
        for second_sample in cluster.samples:
            total += Sample.compute_euclidean_distance(sample, second_sample)
        curr_out = total / len(cluster.samples)
        if curr_out < smallest:
            smallest = curr_out
        total = 0
    return smallest


def find_dominant_label(cluster):
    """
    :param cluster: a cluster
    :return: the dominant sample of the cluster
    """
    max = 0
    histogram = {}
    dominant_label = ""
    for sample in cluster.samples:
        histogram[sample.label] = 0
    for sample in cluster.samples:
        histogram[sample.label] += 1
    for i, key in enumerate(histogram.keys()):
        if histogram[key] > max:
            max = histogram[key]
            dominant_label = list(histogram.keys())[i]
    return str(dominant_label)


def find_min(mat, length):
    """
    :param mat: a matrix
    :param length: the length of the row
    :return: the min value in the matrix
    """
    mini = float('inf')
    index = []
    temp_i = 0
    temp_j = 0
    for i in range(length):
        for j in range(i):
            value = mat[i][j]
            if mini > value > 0:
                mini = value
                temp_i = i
                temp_j = j
    index.append(temp_i)
    index.append(temp_j)
    return index


def initialize(matrix, i, len):
    """
    :param matrix: a mat
    :param i: an index
    :param len: length of rows
    :return: a mat with initialized i row
    """
    for j in range(i):
        matrix[i][j] = float('inf')
    for k in range(i, len):
        matrix[k][i] = float('inf')


def find_clusters(sample, other_sample, clusters):
    """
    :param sample: a sample
    :param other_sample: other sample
    :param clusters:list of clusters
    :return: the clusters to which the samples belong
    """
    clusters_id = []
    for cluster in clusters:
        if sample in cluster.samples:
            clusters_id.append(cluster.c_id)
        if other_sample in cluster.samples:
            clusters_id.append(cluster.c_id)
    return clusters_id
