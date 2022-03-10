import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv
import transform_graph
import get_core_nodes

#graph_path = 'C:/Users/ASUS/Desktop/project/Core-periphery-Structures/dataset/soc-sign-bitcoinotc.csv'
graph_path = 'dataset/soc-sign-bitcoinotc.csv'
# graph_path = 'dataset/soc-sign-bitcoinalpha.csv'

G = transform_graph.transform_graph(graph_path)
print(nx.info(G))

# Get the list of core nodes
core_nodes, periphery_nodes = get_core_nodes.get_core_nodes(graph_path)

# Get the list of core nodes'edges
core_edges = G.edges(core_nodes, data=True)

# print(core_edges)

num_of_core_edges = len(core_edges)

print("Total number of core node's edges: ", num_of_core_edges)



periphery_edges = G.edges(periphery_nodes, data=True)
num_of_periphery_edges = len(periphery_edges)
print("Total number of periphery node's edges: ", num_of_periphery_edges)


edge_weight = 0

for u, v, w in core_edges:
    # print(w['weight'])
    edge_weight += w['weight']

print("Total weight of core node's edges: ", edge_weight)

avg_weight = edge_weight/num_of_core_edges

print("Average weight of core node's edges: ", avg_weight)


# file = open("result/bitcoinotc.csv", "w", newline='')  # make the result as a csv file
# # file.write('Name\tPairID\tCoreness\n')
# writer = csv.writer(file)
# writer.writerow(['Name', 'PairID', 'Coreness'])

# for key, value in sorted(c.items(), key=lambda x: x[1]):
#     # file.write('%s\t%d\t%f\n' %(key, c[key], x[key]))
#     i ={key, c[key], x[key]}
#     print(i)
#     writer.writerow(i)
# file.close()


# fig = plt.figure(figsize=(8, 6))
# ax = plt.gca()
# ax, pos = cpnet.draw(G, c, x, ax)
# ax, _ = cpnet.draw(G, c, x, ax, pos=pos)
# nx.draw_networkx_labels(G, pos)

# plt.show()