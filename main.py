import sys
from data import Data
from sample import Sample
from agglomerative_clustering import AgglomerativeClustering
from link import SingleLink, CompleteLink


def main(argv):
    data_dict = Data(argv[1])
    list_of_samples = data_dict.create_samples()

    single_link = SingleLink()
    single_clustering = AgglomerativeClustering(single_link, list_of_samples)
    print("single link:")
    AgglomerativeClustering.run(single_clustering, 7)
    complete_link = CompleteLink()
    complete_clustering = AgglomerativeClustering(complete_link, list_of_samples)
    print("")
    print("complete link:")
    AgglomerativeClustering.run(complete_clustering, 7)


if __name__ == '__main__':
    main(sys.argv)
