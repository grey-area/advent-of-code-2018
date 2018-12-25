import numpy as np
from scipy.spatial import KDTree
from scipy.sparse import csc_matrix
from scipy.sparse.csgraph import connected_components

data = np.loadtxt('input', delimiter=',')
N = data.shape[0]

tree = KDTree(data)
pairs = tree.query_pairs(3, p=1)
rows, cols = list(zip(*pairs))
sparse_graph = csc_matrix((np.ones_like(rows), (rows, cols)),  (N, N))

ans = connected_components(sparse_graph, directed=False, return_labels=False)
print(ans)
