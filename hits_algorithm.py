import networkx as nx
from pprint import pprint
import pandas as pd
import numpy as np


def main():

    edge_list = [('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'A'),
                 ('D', 'C'), ('E', 'D'), ('E', 'B'), ('E', 'F'),
                 ('E', 'C'), ('C', 'H'), ('G', 'A'),
                 ('G', 'C'), ('H', 'A'), ('F', 'B')]

    node_set = set()
    for edge in edge_list:
        node_a, node_b = edge
        node_set.add(node_a)
        node_set.add(node_b)

    node_list = sorted(list(node_set))

    G = nx.DiGraph()
    G.add_nodes_from(node_list)
    G.add_edges_from(edge_list)

    adj_matrix = nx.to_numpy_matrix(G)

    # adj_list = nx.to_dict_of_lists(G)
    # pprint("隣接リスト")
    # pprint(adj_list)

    df_adj = pd.DataFrame(
        adj_matrix,
        columns=node_list,
        index=node_list,
        dtype="int64")
    pprint("隣接行列")
    pprint(df_adj)

    auth, hub = calc_hits_algorithm(adj_matrix=adj_matrix)

    df_auth = pd.DataFrame(
        auth,
        columns=["authority"],
        index=node_list
    )

    df_hub = pd.DataFrame(
        hub,
        columns=["hubs"],
        index=node_list
    )

    df_result = pd.concat([df_auth, df_hub], axis=1)

    pprint("Result")
    pprint(df_result)

    # print(adj_matrix.shape)
    # a = np.array([[1, 1, 1]])
    # a_r = np.c_[a]
    # print(a.shape)
    # print(a_r.shape)


def calc_hits_algorithm(adj_matrix, iter=60, normalize=True, delta=1e-8):
    g, r = adj_matrix.shape
    auth = np.ones((g, 1))
    hub = np.ones((g, 1))

    L = adj_matrix

    for k in range(iter):

        auth_k_1 = auth
        hub_k_1 = hub

        auth = L.T @ L @ auth
        hub = L @ L.T @ hub

        if normalize:
            auth_l1_norm = np.linalg.norm(auth, ord=1)
            hub_l1_norm = np.linalg.norm(hub, ord=1)
            auth = auth / auth_l1_norm
            hub = hub / hub_l1_norm

        delta_auth = np.linalg.norm(auth - auth_k_1, ord=1)
        delta_hub = np.linalg.norm(hub - hub_k_1, ord=1)

        if delta_auth < delta and delta_hub < delta:
            print("iter count : ", k)
            return auth, hub

    print("iter count : ", k)
    return auth, hub


if __name__ == "__main__":
    main()
