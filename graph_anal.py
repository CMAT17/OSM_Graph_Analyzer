import osmnx as ox
import networkx as nx
from scipy.sparse import csgraph as sc
import json

def all_pairs_sp(G):
    #print(G.edges(data = True))
    paths = floyd_warshall(G,weight = 'length')
    with open("all_pairs_sp_dict.txt", "w") as file:
        file.write(json.dumps(paths))

def main():
    G = nx.read_gpickle('./SJ.gpickle')
    #ox.plot_graph(G)

    T = G.copy()

    for (n,d) in T.nodes(data = True):
        d.clear()

    print(T.nodes(data = True))

    input('Press enter to continue')

    for (n1,n2,d) in T.edges(data = True):
        len_val = d['length']
        d.clear()
        d['length'] = len_val

    print(T.edges(data = True))
    #all_pairs_sp(T)

    T_adj = nx.to_scipy_sparse_matrix(T,weight = "length")

    final_dist_mtx = sc.floyd_warshall(T_adj, directed = False, unweighted = True)

    print(final_dist_mtx)

if __name__ == "__main__":
    main()
