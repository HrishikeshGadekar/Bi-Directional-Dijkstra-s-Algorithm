import math
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import pylab
import seaborn as sns

# Initialization of an Empty Network Graph:
G = nx.DiGraph()

# The Graph is input from Input_CSV.csv file:
n = int(input('Enter the number of Nodes: '))
print('')

df = pd.read_csv('Input_CSV.csv')
dfpi = pd.DataFrame(df)

nan = int(0)
df = df.fillna(nan)  # The unfilled places in CSV file are filled with integer 0 which indicates the arc (i,j) does not exist
df = df.astype('int64')  # Type conversion of all Nodes and Costs entries to integer

# The Cost matrix is extracted as follows in a (n x n) square matrix:
dfp = df.iloc[0:(n + 1), 0:(n + 1)]

dfg = df.iloc[0:n, 0:(n + 1)]
print('The Cost matrix is: \n', dfg)
print('')

node_list = list(i for i in range(1, (n + 1)))  # A List of all Nodes in the Graph,

edges = list()  # A List of Edges in the Graph
weights = list()  # A List of Weights of all the existent Edges
edge_weights = list()  # A list of triplets containing (i, j, cost(i, j))

# The following for loop compiles Edges & Weights data:
for i in range(0, n + 1):
    for j in range(1, n + 1):
        if dfp.iloc[i, j] != 0:
            edges.append((i + 1, j))
            weights.append(dfp.iloc[i, j])
            edge_weights.append((i + 1, j, dfp.iloc[i, j]))

# Addition of Nodes, Edges and Weights to the Graph G:
G.add_nodes_from(node_list)
G.add_edges_from(edges)
G.add_weighted_edges_from(edge_weights)

# The Graph will be plotted as follows:
# pos = nx.spring_layout(G)

node_labels = {node: node for node in G.nodes()}
edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

nx.draw_kamada_kawai(G, edge_labels=edge_labels, with_labels=True)
nx.draw_kamada_kawai(G, labels=node_labels, node_color='skyblue', node_size=500, edge_cmap=plt.cm.Reds, edge_color='black')

plt.show()  # To show the Graph figure