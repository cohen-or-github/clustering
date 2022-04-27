from sample import Sample
from cluster import Cluster
from static_functions import in_xy, out_xy, find_min, initialize, find_clusters
from link import Link


class AgglomerativeClustering:
    def __init__(self, link, samples):
        """
        :param link: single link / complete link object
        :param samples: list of Samples objects
        """
        self.link = link
        self.samples = samples
        self.clusters_list = []
        for sample in self.samples:
            new_object = Cluster(sample.s_id, [sample])
            self.clusters_list.append(new_object)

    def compute_silhoeutte(self, new_clusters):
        """
        building dictionary of the silhoeutte value for each point
        :return: dictionary, with samples ids as keys and the sample's silhoeutte as value
        """
        dictionary_of_samples = {}
        for cluster in new_clusters:
            if len(cluster.samples) > 1:
                for sample in cluster.samples:
                    in_sample = in_xy(sample, cluster)
                    out_sample = out_xy(new_clusters, cluster, sample)
                    dictionary_of_samples[sample.s_id] = (out_sample - in_sample) / (max(in_sample, out_sample))
            else:
                for sample in cluster.samples:
                    dictionary_of_samples[sample.s_id] = 0
        return dictionary_of_samples

    def compute_summery_silhoeutte(self, new_clusters_list):
        """
        :param new_clusters_list: a list of clusters
        :return: a dictionary in which the keys are clusters ids  & their values are the silhoeutte's value
        """
        samples_dict = self.compute_silhoeutte(new_clusters_list)
        dictionary_of_clusters = {}
        total = 0
        for cluster in new_clusters_list:
            total = 0
            for sample in cluster.samples:
                total += samples_dict[sample.s_id]
            dictionary_of_clusters[cluster.c_id] = total / len(cluster.samples)
        s_dataset = sum(samples_dict.values()) / len(samples_dict.keys())
        dictionary_of_clusters[0] = s_dataset
        return dictionary_of_clusters

    def compute_rand_index(self, new_clusters):
        """
        :param new_clusters: list of clusters
        :return: the rand value
        """
        tp = 0
        tn = 0
        length = len(self.samples)
        ncr = length * (length - 1) / 2
        for i in range(length):
            for j in range(i + 1, length, 1):
                sample = self.samples[i]
                other_sample = self.samples[j]
                clusters = find_clusters(sample, other_sample, new_clusters)
                if sample.label == other_sample.label and clusters[0] == clusters[1]:
                    tp += 1
                if sample.label != other_sample.label and clusters[0] != clusters[1]:
                    tn += 1
        return (tp + tn) / ncr

    def run(self, max_clusters):
        """
        :param max_clusters: the max number of clusters we can divide our samples to
        :return: void
        """
        num_of_clusters = len(self.clusters_list)
        original_len = num_of_clusters
        distance_mat = [[0 for x in range(num_of_clusters)] for y in range(num_of_clusters)]

        for i in range(num_of_clusters):
            for j in range(i):
                distance_mat[i][j] = type(self.link).compute(self.link, self.clusters_list[i], self.clusters_list[j])
        index_list = list(range(0, num_of_clusters))

        while num_of_clusters > max_clusters:
            to_merge = find_min(distance_mat, original_len)
            first_cluster = to_merge[0]
            second_cluster = to_merge[1]
            Cluster.merge(self.clusters_list[second_cluster], self.clusters_list[first_cluster])
            index_list.remove(first_cluster)
            num_of_clusters -= 1
            initialize(distance_mat, max(first_cluster, second_cluster), original_len)

            for i in index_list:
                if i < second_cluster:
                    distance_mat[second_cluster][i] = type(self.link)\
                                                    .compute(self.link, self.clusters_list[second_cluster],
                                                    self.clusters_list[i])
                if i > second_cluster:
                    distance_mat[i][second_cluster] = type(self.link).compute(self.link,
                                                            self.clusters_list[second_cluster],
                                                            self.clusters_list[i])

        new_clusters = []
        for index in index_list:
            new_clusters.append(self.clusters_list[index])

        silhouette_dict = self.compute_summery_silhoeutte(new_clusters)
        for cluster in new_clusters:
            Cluster.print_details(cluster, silhouette_dict[cluster.c_id])

        print("Whole data: silhouette = " + str(round(silhouette_dict[0], 3)), " RI = " +
              str(round(self.compute_rand_index(new_clusters), 3)))


