import osmnx as ox
import networkx as nx
from networkx.algorithms.shortest_paths.dense import floyd_warshall as floyd_warshall
import json

def all_pairs_sp(G):
    #print(G.edges(data = True))
    paths = floyd_warshall(G,weight = 'length')
    with open("all_pairs_sp_dict.txt", "w") as file:
        file.write(json.dumps(paths))

def main():
    G = nx.read_gpickle('SJ.gpickle')
    ox.plot_graph(G)

    all_pairs_sp(G)

if __name__ == "__main__":
    main()
