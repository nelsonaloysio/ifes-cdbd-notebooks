# -*- coding: utf-8 -*-
# see quiser usar acentuação em seus programas use a linha acima.

# módulo para manipulação de grafos
import networkx as nx

# módulo para visualização
import matplotlib.pyplot as plt
#import pylab as plt

# cria um (objeto) grafo vazio
G=nx.Graph()

# adiciona nós e arestas
G.add_edge("Node1", "Node2")

#adiciona nó
G.add_node("Node3")

# plota o grafo
nx.draw(G, with_labels = True)
plt.show()

#caso queira salva uma imagem, use o comando abaixo
#plt.savefig('grafo_aula-1-1.png')
