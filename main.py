import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib import cm
import numpy as np
import random


# fonction chopisissant le poids au hasard
def GenerateWeight():
    return round(random.uniform(0, 1), 1)


# défini les noeuds, arrëëtes, et poid du graphe

A = np.array([[0, 0.4, 0.6],
              [0.5, 0, 0.5],
              [0.3, 0.7, 0]])
# génère le graphe

G = nx.DiGraph(A)
pos = nx.spring_layout(G)

# divise le graph en 2 opinions
u = np.ones(3)
for j in range(3 // 2):
    u[2 * j] = 0



# Tracé de la condition initiale
fig = plt.figure(1)
nx.draw(G, with_labels=True, pos=pos, node_color=u, cmap='coolwarm')

labels = nx.get_edge_attributes(G, 'weight')
sc = nx.draw_networkx_nodes(G, pos, node_color=u, cmap='coolwarm')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.3)


# matrix
M = nx.to_numpy_array(G)

print("Matrice d\'adjacence: \n", M)

# affiche le graphe et la légende

fig.colorbar(sc)
plt.title("Opinion initiale")
plt.show()
