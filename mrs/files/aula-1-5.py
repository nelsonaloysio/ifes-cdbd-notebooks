# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

f = open('grafo.txt')    # open the example file
lines = f.readlines()    # read lines of file and stores in lines var.

# for each line in variable 'lines' do...
for line in lines:
    # string manipulation:
    #    1) split('\t'): separates the current line in columns ('\t' separator)
    #    2) strip(): removes white chars from each column element
    #                (ex: '\n', white spaces, etc)
    fields = line.strip().split('\t')
    # Exercise 1: put some code here to dealing exception, like *empty lines*
    # Exercise 2: explain why an empty line will generate an error (index out of bounds).
    #
    # retrieve the first and the second column for each line
    u = fields[0]
    v = fields[1]
    # adds the edge (u,v) to the graph 
    G.add_edge(u,v)

# after reading everything, closes the file.
f.close()



print("Nós do grafo G: ")
print(G.nodes())

print("Arestas do grafo G: ")
print(G.edges())

nx.draw(G, with_labels = True)
plt.show()

