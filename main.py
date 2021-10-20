import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time


# fonction chopisissant le poids au hasard
def GenerateWeight():
    return round(random.uniform(0, 1), 1)


# défini les noeuds, arrëëtes, et poid du graphe

# A = np.array([[0, 0.4, 0.6],
#             [0.4, 0, 0.5],
#            [0.3, 0.7, 0]])

A = np.array([[0, 0.5, 0.3],
              [0.4, 0, 0.7],
              [0.6, 0.5, 0]])
# génère le graphe
G = nx.DiGraph(A)
pos = nx.spring_layout(G)
# divise le graph en 2 opinions
color = ([1, 0, 1])


def run():
    # Tracé de la condition initiale
    fig = plt.figure(1)
    nx.draw(G, with_labels=True, pos=pos, node_color=color, cmap='coolwarm')
    labels = nx.get_edge_attributes(G, 'weight')
    sc = nx.draw_networkx_nodes(G, pos, node_color=color, cmap='coolwarm', vmin=0, vmax=1)  # affiche echelle
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.2)  # affiche pos

    print(color)
    # affiche le graphe et la légende
    plt.axis('equal')
    fig.colorbar(sc)  # affiche echelle
    plt.title("Opinion initiale")
    plt.show()


def getMatrix():
    M = nx.to_numpy_array(G)
    print("Matrice d\'adjacence: \n", M)


for i in range(10):
    run()
    color = np.dot(color, A)
    time.sleep(1)
