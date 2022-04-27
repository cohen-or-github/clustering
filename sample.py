class Sample:
    def __init__(self, s_id, genes, label):
        """
        :param s_id: identification number
        :param genes: a list of the values of the sample's genes
        :param label: a string that represent the value of the sample in the 'type' row
        """
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def __repr__(self):
        return "{}, {}, {}".format(self.s_id, self.label, self.genes)

    def compute_euclidean_distance(self, other):
        """
        :param other: other point
        :return: the euclidean distance between the points
        """
        total = 0
        for i in range(len(self.genes)):
            total += ((self. genes[i] - other.genes[i])**2)
        return total**0.5

