import torch
from torch_geometric.data import Data
from torch_geometric.data import InMemoryDataset as  IMD

class MyOwnDataset(IMD):
    def __init__(self,root,transformers=None,pre_transfor=None):
        super(MyOwnDataset,self).__init__(root,transformers=None,pre_transfor=None)
        self.data,self.slices=torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self) :
        return ['some_file_1','some_file_2',...]

    @property
    def processed_file_names(self):
        return ['data.pt']

    @property
    def download(self):
        pass

    @property
    def process(self):

        data_list=[...]

        if self.pre_filter is not None:
            data_list=[data for data in data_list if self.pre_filter(data)]
        if self.pre_transform is not None:
            data_list=[self.pre_transform for data in data_list]
        data,slices=self.collate(data_list)
        torch.save((data,slices),self.processed_paths[0])