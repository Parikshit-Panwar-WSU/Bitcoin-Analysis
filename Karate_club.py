import cpnet
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

G = nx.karate_club_graph()
print(G)

kmconfig = cpnet.KM_config()
kmconfig.detect(G)
c = kmconfig.get_pair_id()
x = kmconfig.get_coreness()
print(c)
print(x)
fig = plt.figure(figsize=(8, 6))
ax = plt.gca()
ax, pos = cpnet.draw(G, c, x, ax)
ax, _ = cpnet.draw(G, c, x, ax, pos=pos)

nx.draw_networkx_labels(G, pos)

plt.show()