import numpy as np

# function: build_prob_matrix
# inputs:   adj_list    a direct graph of webpages represented as an adjancency list as a Python list of lists
# outputs:  P           a column-stochastic matrix representing a random walk of the webpages as a Markov chain
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

# function: rank
# inputs:   links       a direct graph of webpages represented as an adjancency list as a Python list of lists
#           d           prob. of web surfer to follow links over random jump, 1 minus the damping factor, default 0.85
# outputs:  a Python list of the webpages sorted in descending order of relevance.
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
    v = abs(evects[:, i]) / sum(abs(evects[:, i]))
    # consider using itemgetter from operators
    return [i for i, e in sorted(enumerate(v), key=lambda x: x[1], reverse=True)]