import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet


# read E-R random graph
n= 80
p= 0.1
g = nx.erdos_renyi_graph(n, p, seed=None, directed=False)

algorithm = cpnet.KM_config()
algorithm.detect(g)
b = algorithm.get_pair_id()
y = algorithm.get_coreness()

print (y)
#plot the graph
fig = plt.figure(figsize=(8, 6))
ax = plt.gca()
ax, pos = cpnet.draw(g, b, y, ax)
ax, _ = cpnet.draw(g, b, y, ax, pos=pos)
nx.draw_networkx_labels(g, pos)

plt.show()