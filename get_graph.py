import osmnx as ox
import networkx as nx

def get_graph():
    G = ox.core.graph_from_place('San Jose, California', network_type = 'drive', buffer_dist = 15000.0)
    print(G.edges(data = True))
    print(G.number_of_nodes())
    #ox.plot_graph(G)
    nx.write_gpickle(G, 'SJ.gpickle') 

if __name__ == "__main__":
    get_graph()