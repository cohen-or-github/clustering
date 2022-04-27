import pandas
from sample import Sample


class Data:
    def __init__(self, path):
        """
        :param path: the path to the file from which we take the data
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        list_of_samples = []
        for index, identity in enumerate(self.data['samples']):
            s_id = identity
            label = self.data['type'][index]
            list_of_genes = []
            keys_list = list(self.data.keys())
            for i in range(2, len(self.data.keys())):
                key = keys_list[i]
                list_of_genes.append(self.data[key][index])
            sample_to_add = Sample(s_id, list_of_genes, label)
            list_of_samples.append(sample_to_add)
        return list_of_samples

