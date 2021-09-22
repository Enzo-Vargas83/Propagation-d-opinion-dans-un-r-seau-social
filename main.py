import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def GenerateWeight():
    return round(random.uniform(0, 1), 1)


# d = {'A':['B','C'],'B':['A','D'],'C':['A','D'],'D':['C','B'],'E':['A','B','C','D']}

d = {'A': ['B'], 'B': ['C'], 'C': ['A']}    # dictionnaire des arrête et sommet

G = nx.DiGraph(d) # génération du graph

# poids
G.add_edges_from([
    ('A', 'B', {'weight': GenerateWeight()}),
    ('B', 'C', {'weight': GenerateWeight()}),
    ('C', 'A', {'weight': GenerateWeight()})
])
# met les poid au arrette
pos = nx.spring_layout(G)


nx.draw(G, with_labels=True, pos=pos) #add label

labels = nx.get_edge_attributes(G, 'weight')  #show weight
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print("Matrice d\'adjacence : \n", nx.to_numpy_array(G))

plt.show()

# https://networkx.org/documentation/stable/reference/generated/networkx.linalg.graphmatrix.adjacency_matrix.html

