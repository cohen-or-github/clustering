import static_functions

class Cluster:
    def __init__(self, c_id, samples):
        """
        :param c_id: the cluster's id
        :param samples: list of objects from type Samples
        """
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        """
        :param other: another cluster
        :return: a merge between the 2 clusters
        """
        new_id = static_functions.minimum(self.c_id, other.c_id)
        for sample in other.samples:
            self.samples.append(sample)
        self.samples.sort(key=lambda x: x.s_id)
        self.c_id = new_id
        del other

    def print_details(self, silhouette):
        """
        :param silhouette: the value of the silhouette
        :return: void
        """
        print_string = ""
        print_string += "Cluster " + str(self.c_id) + ": "
        num_of_samples = []
        dominant_label = static_functions.find_dominant_label(self)

        for sample in self.samples:
            num_of_samples.append(sample.s_id)

        sorted_list = sorted(num_of_samples)
        print_string += str(sorted_list) + ", dominant label = " + dominant_label + ", silhouette = " \
                        + str(round(silhouette, 3))
        print(print_string)

