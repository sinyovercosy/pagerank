import numpy as np

def build_prob_matrix(adj_list):
    # number of nodes
    n = len(adj_list)
    P = np.zeros((n,n), dtype=float)
    for (j, connected_nodes) in enumerate(adj_list):
        if connected_nodes: # non-empty
            P[connected_nodes, j] = 1.0 / len(connected_nodes)
        else: # dangling node
            P[:, j] = 1.0 / n
    return P

def rank(links, d=0.85):
    n = len(links)
    P = build_prob_matrix(links)
    M = d * P + (1 - d) / n * np.ones(P.shape)
    # consider using power method and sparse multiplication to approx evects
    (evals, evects) = np.linalg.eig(M)
    # index of evect corresponding to 1
    # i = np.where(np.isclose(evals, 1.0))
    # below is faster, from https://stackoverflow.com/questions/41022765
    i = next(i for i, e in enumerate(evals) if np.isclose(e, 1.0)) 
    v = evects[:, i] / sum(evects[:, i])
    # consider using itemgetter from operators
    return [i for i, e in sorted(enumerate(v), key=lambda x: x[1], reverse=True)]