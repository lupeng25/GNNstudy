# import torch
# import networkx as nx
# import matplotlib.pyplot as plt
#
# # Visualization function for NX graph or PyTorch tensor
# def visualize(h, color, epoch=None, loss=None):
#     plt.figure(figsize=(7,7))
#     plt.xticks([])
#     plt.yticks([])
#
#     if torch.is_tensor(h):
#         h = h.detach().cpu().numpy()
#         plt.scatter(h[:, 0], h[:, 1], s=140, c=color, cmap="Set2")
#         if epoch is not None and loss is not None:
#             plt.xlabel(f'Epoch: {epoch}, Loss: {loss.item():.4f}', fontsize=16)
#     else:
#         nx.draw_networkx(G, pos=nx.spring_layout(G, seed=42), with_labels=False,
#                          node_color=color, cmap="Set2")
#     plt.show()
# from torch_geometric.datasets import KarateClub
#
# dataset = KarateClub()
# print(f'Dataset: {dataset}:')
# print('======================')
# print(f'Number of graphs: {len(dataset)}')
# print(f'Number of features: {dataset.num_features}')
# print(f'Number of classes: {dataset.num_classes}')
# print(dataset.num_node_features)
# print(dataset.num_edge_features)
# print(dataset.len())
# data = dataset[0]  # Get the first graph object.
#
# print(data)
# print('==============================================================')
#
# # Gather some statistics about the graph.
# print(f'Number of nodes: {data.num_nodes}')
# print(f'Number of edges: {data.num_edges}')
# print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}')
# print(f'Number of training nodes: {data.train_mask.sum()}')
# print(f'Training node label rate: {int(data.train_mask.sum()) / data.num_nodes:.2f}')
# print(f'Contains isolated nodes: {data.contains_isolated_nodes()}')
# print(f'Contains self-loops: {data.contains_self_loops()}')
# print(f'Is undirected: {data.is_undirected()}')
# from torch_geometric.utils import to_networkx
#
# G = to_networkx(data, to_undirected=True)
# visualize(G, color=data.y)
# import torch
# from torch.nn import Linear
# from torch_geometric.nn import GCNConv
#
#
# class GCN(torch.nn.Module):
#     def __init__(self):
#         super(GCN, self).__init__()
#         torch.manual_seed(12345)
#         self.conv1 = GCNConv(dataset.num_features, 4)
#         self.conv2 = GCNConv(4, 4)
#         self.conv3 = GCNConv(4, 2)
#         self.classifier = Linear(2, dataset.num_classes)
#
#     def forward(self, x, edge_index):
#         h = self.conv1(x, edge_index)
#         h = h.tanh()
#         h = self.conv2(h, edge_index)
#         h = h.tanh()
#         h = self.conv3(h, edge_index)
#         h = h.tanh()  # Final GNN embedding space.
#
#         # Apply a final (linear) classifier.
#         out = self.classifier(h)
#
#         return out, h
#
# model = GCN()
# print(model)
# model = GCN()
#
# _, h = model(data.x, data.edge_index)
# print(f'Embedding shape: {list(h.shape)}')
#
# visualize(h, color=data.y)



