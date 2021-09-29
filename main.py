import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

#fonction chopisissant le poids au hasard
def GenerateWeight():
   return round(random.uniform(0, 1), 1)

#défini les noeuds, arrëëtes, et poid du graphe
d = {'A':{'B':{'weight': GenerateWeight()}, 'C':{'weight':GenerateWeight()}}, 
'B':{'C':{'weight':GenerateWeight()}, 'D':{'weight':  GenerateWeight()}}, 
'C': {'D':{'weight':GenerateWeight()}}}

#génère le graphe
G = nx.DiGraph(d)
pos = nx.spring_layout(G)

#divise le graph en 2 opinions
u = np.ones(4)
for j in range(4//2):
    u[2*j]=0

# Tracé de la condition initiale
fig=plt.figure(1)
nx.draw(G, with_labels=True,pos=pos,node_color=u, cmap='coolwarm')
labels = nx.get_edge_attributes(G, 'weight')
sc=nx.draw_networkx_nodes(G, pos, node_color=u, cmap='coolwarm')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#matrix 
M = nx.to_numpy_array(G)
print("Matrice d\'adjacence: \n", M)
#addition colonne 
print ('add \n')
s = np.sum(M, axis=1)
#additionne les collonne de la matrix
print(s)






#test influence d'Enzo
M= nx.to_numpy_array(G)
M.T

#calcul du nombre d'adjacent
nbadj = 0
for i in M.T[1]:
    if i != 0:
        nbadj+=1

print("Colonne : \n", M.T[1])
print("Moyenne : \n", sum(M.T[1]/nbadj))
print("Matrice d\'adjacence : \n", nx.to_numpy_array(G))

#affiche le graphe et la légende
plt.axis('equal')
fig.colorbar(sc)
plt.title("Opinion initiale")
plt.show()