# -*- coding: utf-8 -*-
import networkx as nx

G = nx.Graph()

edges = [('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2)]

G.add_weighted_edges_from(edges)


# plota o grafo
nx.draw(G, with_labels = True)
plt.show()


print("Nós do grafo G: ")
print(G.nodes())

print("Arestas do grafo G: ")
print(G.edges())

print("Caminho mínimo entre 'a' e 'd':")
print(nx.dijkstra_path(G,'a','d'))
