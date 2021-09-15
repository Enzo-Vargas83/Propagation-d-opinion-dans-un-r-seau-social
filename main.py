import networkx as nx
import matplotlib.pyplot as plt

# On crée un graphe vide
G = nx.Graph()

# On ajoute les sommets
G.add_node(1)  # un sommet
G.add_nodes_from([2, 3])  # une liste de sommets

nouveaux_noms = {0:'A', 1:'B', 2:'C', 3}
G = nx.relabel_nodes(G, nouveaux_noms)

G.add_edge(1, 2)  # une arête
G.add_edges_from([(1, 3), (2, 1)])  # une liste d'arêtes

# Si on ajoute une arete avec un sommet inconnu celui-ci sera automatiquement créé
G.add_edge(1, 4)

nx.draw(G, with_labels=True, pos=nx.spring_layout(G))  # Tracé du graphe (argument pos optionnel)
plt.show()