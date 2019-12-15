# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# adiciona uma lista de arestas em um único comando
G.add_edges_from([
    ('A', 'B'),    
    ('B', 'C'),    
    ('B', 'F'),    
    ('C', 'D'),    
    ('C', 'E'),    
    ('D', 'E'),    
    ('D', 'F'),
    ('D', 'G'),
    ('E', 'T'),    
    ('F', 'G'),    
    ('G', 'T')    
    ])


print("Nós do grafo G: ")
print(G.nodes())

print("Arestas do grafo G: ")
print(G.edges())

print("Caminho mínimo entre 'A' e 'T':")
print(nx.dijkstra_path(G,'A','T'))

nx.draw(G, with_labels = True)
plt.show()

