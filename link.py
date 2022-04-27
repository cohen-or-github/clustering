from sample import Sample


class Link:
    def compute(self, cluster, other):
        """
        :param cluster: a cluster
        :param other: a diffrent cluster
        :return: void
        """
        pass


class SingleLink(Link):
    def compute(self, cluster, other):
        """
        :param cluster: a cluster
        :param other: another cluster
        :return: the distance between cluster to other by single link method
        """
        minimum = float('inf')
        for idx1, sample1 in enumerate(cluster.samples):
            for idx2, sample2 in enumerate(other.samples):
                distance = Sample.compute_euclidean_distance(sample1, sample2)
                if minimum > distance:
                    minimum = distance
        return minimum


class CompleteLink(Link):
    def compute(self, cluster, other):
        """
        :param cluster: a cluster
        :param other: another cluster
        :return: the distance between cluster to other by complete link method
        """
        maximum = 0
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                distance = Sample.compute_euclidean_distance(sample1, sample2)
                if maximum < distance:
                    maximum = distance
        return maximum
