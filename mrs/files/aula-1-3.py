# -*- coding: utf-8 -*-

import networkx as nx

import matplotlib.pyplot as plt


G = nx.Graph()

# adiciona uma lista de arestas em um único comando
G.add_edges_from([
    ('A', 'B'),    
    ('A', 'C'),    
    ('A', 'D'),    
    ('B', 'E'),    
    ('B', 'F'),    
    ('C', 'F'),    
    ('C', 'G'),    
    ('D', 'G'),    
    ('D', 'H'),
    ('E', 'I'),    
    ('F', 'I'),    
    ('F', 'J'),    
    ('G', 'J'),    
    ('H', 'K'),    
    ('I', 'L'),
    ('J', 'L'),
    ('K', 'L')
    ])

# plota o grafo
nx.draw(G, with_labels = True)
plt.show()
