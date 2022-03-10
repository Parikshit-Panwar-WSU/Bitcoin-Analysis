import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cpnet
import csv

# transform the format of the graph, add weight to edge
# graph_path = 'dataset/soc-sign-bitcoinotc.csv'

def transform_graph (graph_path):
    G = nx.DiGraph()
    for d in pd.read_csv(graph_path,sep=',', header=None, usecols=[0,1,2], names=['source', 'target', 'weight'], chunksize=100):
        G.add_weighted_edges_from([tuple(x) for x in d.values])
    # print(nx.info(G))

    # output the transformed graph
    # df = pd.DataFrame(G.edges(data=True), columns = ['source', 'target', 'weight'])
    # df.set_index('source', inplace=True)
    # df.to_csv('result/bitcoin/bitcoinotc_transformed.csv')
    # df.to_csv('result/bitcoin/bitcoinalpha_transformed.csv')

    return G
    
# transform_graph(graph_path)
