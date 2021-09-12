import torch
from torch_geometric.data import Data
x=torch.tensor([[2,1],[5,6],[12,0],[3,7]],dtype=torch.float)
y=torch.tensor([0,1,0,1],dtype=torch.float)
edge_index=torch.tensor([[0,1,0,2,3],
                         [1,0,3,1,2]],dtype=torch.long)
