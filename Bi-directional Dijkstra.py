"""CE5290 Group Project: Bidirectional Dijkstra Algorithm"""
import math
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import pylab
import datetime


# Initialization of an Empty Network Graph:
G = nx.DiGraph()

print('')
title = "CE 5290 Group Project_Team 1 : Bidirectional Dijkstra Algorithm"
print(title.center(10, '*'))
print('________________________________________________________________')
# Forward Dijkstra Algorithm is applied from the Source node
# Reverse Dijkstra Algorithm is applied from the Sink node
print('')

# The Graph is input from Input_CSV.csv file:
n = int(input('Enter the number of Nodes: '))
print('')

df = pd.read_csv('Input_CSV.csv')
dfpi = pd.DataFrame(df)


nan = math.inf
df = df.fillna(nan)    # The unfilled places in CSV file are filled with integer 0 which indicates the arc (i,j) does not exist


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
        if dfp.iloc[i, j] != math.inf:
            dfp.iloc[i, j] = int(dfp.iloc[i, j])     # Type conversion of all Nodes and Costs entries to integer
            edges.append((i + 1, j))
            weights.append(int(dfp.iloc[i, j]))
            edge_weights.append((i + 1, j, int(dfp.iloc[i, j])))

# Addition of Nodes, Edges and Weights to the Graph G:
G.add_nodes_from(node_list)
G.add_edges_from(edges)
G.add_weighted_edges_from(edge_weights)

# Set S initialized to Null & Set S1 defined as an all node set.
S = list()
S1 = list(G.nodes())

# Set T initialized to Null & Set T1 defined as an all node set.
T = list()
T1 = list(G.nodes())

R = list()  # R will contain all the reached & explored/unexplored Nodes in Forward Dijkstra
RS = set(R)  # Type conversion to Set
PF = list()  # P will contain the Nodes to be examined in the next iteration

R_rev = list()  # R will contain all the reached & explored/unexplored Nodes
RS_rev = set(R_rev)  # Type conversion to Set
P_rev = list()  # P will contain the Nodes to be examined in the next iteration

print('The Graph Node set is: ', S1)
print('The Edges with associated Costs is: ', edge_weights)

# The Graph will be plotted as follows:
node_labels = {node: node for node in G.nodes()}
edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

nx.draw_kamada_kawai(G, edge_labels=edge_labels, with_labels=True)
nx.draw_kamada_kawai(G, labels=node_labels, node_color='skyblue', node_size=500, edge_cmap=plt.cm.Reds, edge_color='black')

plt.show()  # To show the Graph figure

print('')

# The Source and Sink is input by the user:
source = int(input("Please choose the Source node 's': "))
sink = int(input("Please choose the Sink node 't': "))
print('')

a = datetime.datetime.now()     # To measure the time taken, we start here.

# The Dictionary distance_labels_fwd has the forward distance labels for all the nodes:
distance_labels_fwd = dict()
# The Dictionary distance_labels_rev has the reverse distance labels for all the nodes:
distance_labels_rev = dict()

# The Dictionary pred will keep the Predecessors list:
pred = dict()
# The Dictionary succ will keep the Successors list:
succ = dict()

# This for loop will initialize Distance labels as - Source src to 0 & rest of the nodes to infinity:
for i in S1:
    if i == source:
        distance_labels_fwd[i] = 0
    else:
        distance_labels_fwd[i] = math.inf

print('The Distance labels in Forward are: ', distance_labels_fwd)

# This for loop will initialize labels as - Source src to 0 & rest of the nodes to infinity:
for i in T1:
    if i == sink:
        distance_labels_rev[i] = 0
    else:
        distance_labels_rev[i] = math.inf

print('The Distance labels in Reverse are: ', distance_labels_rev)

print('---------------------------------------------------------------------------------------------------------------')

# Iterations begin now:

## Iteration 1 for Forward is as follows:
iteration = 1
if iteration == 1:
    print('')
    print('Iteration Number: 1')
    print('___________________')
    print('Forward Dijkstra -')
    print('The smallest labelled unexplored Node is: ', source)

    # List of Values in distance_labels
    list_dist_labels_vals = list(distance_labels_fwd.values())
    # List of Keys in distance_labels
    list_dist_labels_keys = list(distance_labels_fwd.keys())

    smallest_label_value = min(list_dist_labels_vals)

    # The following list will contain all the nodes adjacent to the smallest labelled node
    # (list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]) - Gives the key to the value (smallest_label_value) from the list of keys
    adj_list = list(G.adj[list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]])

    # Arc Processing for iteration 1 in Forward Dijkstra:
    for h in adj_list:
        if distance_labels_fwd[h] > distance_labels_fwd[
            list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]] + \
                G[list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]][h]['weight']:
            distance_labels_fwd[h] = distance_labels_fwd[
                                         list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]] + \
                                     G[list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]][h][
                                         'weight']
            pred[h] = list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]
            PF.append(h)
            R.append(h)

    # Set S will now contain the Source node 'src':
    S.append(source)
    # Set R will now contain the Source node 'src' as reached:
    R.append(source)
    # The withdrawal of Source node from set S1:
    S1.remove(source)

    print('The set S is: ', S)
    print('The set S1 is: ', S1)
    print('The updated Distance labels are: ', distance_labels_fwd)
    print('The list of Predecessors is: ', pred)

    ## Iteration 1 for Reverse is as follows:
    if iteration == 1:
        print('')
        print('Reverse Dijkstra -')
        print('The smallest labelled unexplored Node is: ', sink)

        # List of Values in distance_labels
        list_dist_labels_vals = list(distance_labels_rev.values())
        # List of Keys in distance_labels
        list_dist_labels_keys = list(distance_labels_rev.keys())

        smallest_label_value = min(list_dist_labels_vals)

        rev_adjacency_list = list()

        # The following list will contain all the nodes adjacent to the smallest labelled node
        # (list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]) - Gives the key to the value (smallest_label_value) from the list of keys

        for (u, v, wt) in G.edges.data('weight'):
            if v == list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]:
                rev_adjacency_list.append(u)

        # Arc Processing for iteration 1 in Reverse Dijkstra:
        for h in rev_adjacency_list:
            if distance_labels_rev[h] > distance_labels_rev[
                list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]] + \
                    G[h][list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]]['weight']:
                distance_labels_rev[h] = distance_labels_rev[
                                             list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]] + \
                                         G[h][list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]][
                                             'weight']
                succ[h] = list_dist_labels_keys[list_dist_labels_vals.index(smallest_label_value)]
                P_rev.append(h)
                R_rev.append(h)

        # Set T will now contain the Sink node 'sink':
        T.append(sink)
        # Set R_rev will now contain the Sink node 'snk' as reached:
        R_rev.append(sink)
        # The withdrawal of Source node from set T1:
        T1.remove(sink)

        print('The set T is: ', T)
        print('The set T1 is: ', T1)

        S_set = set(S)
        T_set = set(T)

        print('The updated Distance labels in Reverse are: ', distance_labels_rev)
        print('The list of Successors is: ', succ)

S_set = set(S)
T_set = set(T)

print('---------------------------------------------------------------------------------------------------------------')

iteration_number = 2
# The further iterations will be done as follows:
if iteration_number != 1:
    while S_set & T_set == set():
        print('Iteration Number: ', iteration_number)
        print('____________________')
        print('Forward Dijkstra -')

        list_keys = list(distance_labels_fwd.keys())
        list_vals = list(distance_labels_fwd.values())
        dist_labels = list()

        # Finding the smallest label:
        for i in PF:
            dist_labels.append(distance_labels_fwd[i])
        smallest_label = min(dist_labels)

        # The following loop will give the smallest labelled Node to be explored in this iteration:
        for key in distance_labels_fwd:
            if (distance_labels_fwd[key] == smallest_label) and (key not in S):
                smallest_node = key

        print('The smallest labelled unexplored Node is: ', smallest_node)

        # The withdrawal of the smallest labelled node from set S1:
        S1.remove(smallest_node)
        # The addition of the smallest labelled node to set S1:
        S.append(smallest_node)

        print('The set S is: ', S)
        print('The set S1 is: ', S1)

        # The following list will contain all the nodes adjacent to the smallest labelled node
        adjacency_list = list(G.adj[smallest_node])

        # Arc Processing in Forward Dijkstra:
        for h in adjacency_list:
            if distance_labels_fwd[h] > distance_labels_fwd[smallest_node] + G[smallest_node][h]['weight']:
                distance_labels_fwd[h] = distance_labels_fwd[smallest_node] + G[smallest_node][h]['weight']
                # Updating Predecessors list:
                pred[h] = smallest_node

            if h not in PF and h not in R:
                PF.append(h)
                R.append(h)

        PF.remove(smallest_node)

        print('The updated Distance labels are: ', distance_labels_fwd)
        print('The list of Predecessors is: ', pred)

        S_set = set(S)
        RS = set(R)

        # The iteration for Reverse Dijkstra will be done as follows:
        if S_set & T_set == set():         # This if statement checks if we have found the common node yet or not
            print('')
            print('Reverse Dijkstra -')
            list_keys = list(distance_labels_rev.keys())
            list_vals = list(distance_labels_rev.values())

            dist_labels = list()

            # Finding the smallest label:
            for i in P_rev:
                dist_labels.append(distance_labels_rev[i])

            smallest_label = min(dist_labels)

            # The following loop will give the smallest labelled Node to be explored in this iteration:
            for key in distance_labels_rev:
                if (distance_labels_rev[key] == smallest_label) and (key not in T):
                    smallest_node = key

            print('The smallest labelled unexplored Node is: ', smallest_node)

            # The withdrawal of the smallest labelled node from set T1:
            T1.remove(smallest_node)
            # The addition of the smallest labelled node to set T:
            T.append(smallest_node)

            print('The set T is: ', T)
            print('The set T1 is: ', T1)

            rev_adj_list = list()
            # The following list will contain all the nodes adjacent to the smallest labelled node
            for (u, v, wt) in G.edges.data('weight'):
                if v == smallest_node:
                    rev_adj_list.append(u)

            # Arc Processing in Reverse Dijkstra:
            for h in rev_adj_list:
                if distance_labels_rev[h] > distance_labels_rev[smallest_node] + G[h][smallest_node]['weight']:
                    distance_labels_rev[h] = distance_labels_rev[smallest_node] + G[h][smallest_node]['weight']
                    # Updating Successors list:
                    succ[h] = smallest_node

                if h not in P_rev and h not in R_rev:
                    P_rev.append(h)
                    R_rev.append(h)

            P_rev.remove(smallest_node)

            print('The updated Distance labels in Reverse are: ', distance_labels_rev)
            print('The list of Successors is: ', succ)

            RS_rev = set(R_rev)
            T_set = set(T)

            print(
                '------------------------------------------------------------------------------------------------------------')

            iteration_number += 1


## Final Result:
print('---------------------------------------------------------------------------------------------------------------')
print('The Shortest Path distance labels in Forward are as follows: \n', distance_labels_fwd)
print('The Shortest Path distance labels in Reverse are as follows: \n', distance_labels_rev)
print('')

# The Common node found is determined:
common = list(set(S).intersection(T))
common_node = int(common[0])
print('The Common Node found is: ', common_node)

# The Optimal path distance assuming that Shortest path passes through this Common node is calculated:
optimal_path = distance_labels_fwd[common_node] + distance_labels_rev[common_node]
print('')
print('The current optimal path is d1(%d) + d2(%d) = %d' % (common_node, common_node, optimal_path))
print('')

bridge_tail = common_node
bridge_head = common_node
# Optimality Check:
for i in S:
    opt_path = list()
    for j in T:
        if i != j:
            if (i, j) in edges:  # Changed for to if
                op = distance_labels_fwd[i] + G[i][j]['weight'] + distance_labels_rev[j]
                if (op < optimal_path) and ((i != common_node) or (j != common_node)):
                    optimal_path = op
                    bridge_tail = i
                    bridge_head = j
                    print('The Shortest path passes through nodes %d and %d' % (i, j))
                    print('The bridging arc between set S and set T is (%d,%d)' % (i, j))
                    print('')

print('The Shortest Path distance is: ', optimal_path)
print('')
print('The predecessor list: ', pred)

# To find the Shortest Path:
path = []
node = bridge_tail
while node != source:
    path.append(node)
    node = pred[node]
path.append(source)
path.reverse()

node = bridge_head
while node != sink:
    if node not in path:
        path.append(node)
    node = succ[node]
path.append(sink)

print('')
print('---------------------------------------------------------------------------------------------------------------')
print('The Shortest path from Source %d to Sink %d is: ' % (source, sink), path)


# To highlight the Shortest path in the Graph:
def shortest_path(graph):
    red_edges = dict()  # This dictionary will contain arcs from the Shortest Path

    # The following loop identifies the Arcs in the Shortest Path from Source to Sink:
    for (u, v, w) in edge_weights:
        if u in path and v in path and ((path.index(v) - path.index(u)) == 1):
            red_edges[(u, v)] = w

    print('The Shortest Path with the Arc & Costs is: ', red_edges)
    print('---------------------------------------------------------------------------------------------------------------')

    edge_colors = ['black' if not edge in red_edges else 'red' for edge in graph.edges()]
    nx.draw_shell(graph, node_color='yellow', with_labels=True, edge_color=edge_colors)

    pylab.show()  # To show the Graph figure


shortest_path(G)

b = datetime.datetime.now()
delta = b - a
print(delta)
print('The time elapsed in milliseconds is: ', delta.total_seconds() * 1000)  # milliseconds