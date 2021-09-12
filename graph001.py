import torch
from torch_geometric.data import Data
x=torch.tensor([[2,1],[5,6],[12,0],[3,7]],dtype=torch.float)
y=torch.tensor([0,1,0,1],dtype=torch.float)
edge_index=torch.tensor([[0,1,0,2,3],
                         [1,0,3,1,2]],dtype=torch.long)
data=Data(x=x,y=y,edge_index=edge_index)
nu=data.num_nodes+data.num_edge_features+data.num_node_features
+data.contains_isolated_nodes()+data.contains_self_loops()+data.is_directed()
