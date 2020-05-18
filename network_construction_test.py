import numpy as np
import json
from simulator.instance import Instance
from solver.simpleKnapsack import SimpleKnapsack
import networkx as nx
import matplotlib.pyplot as plt
import random


fp = open("./etc/config.json", 'r')
sim_setting = json.load(fp)
#%%########### GRAPH GENERATION ###########
########### NODE GENERATION
g = nx.Graph()
for i in (range(sim_setting["total_node"])):
    nodes = g.add_node(i)
# o = g.order()


########### EDGE GENERATION

c1 = np.random.choice(g.nodes())
c2 = np.random.choice(g.nodes())
if c1 != c2 and g.has_edge(c1,c2) == 0:
    g.add_edge(c1,c2)
for j in (range(sim_setting["total_node"])):
    while (g.degree(j) <= 1):
        c1 = np.random.choice(g.nodes())
        c2 = np.random.choice(g.nodes())
        if c1 != c2 and g.has_edge(c1,c2) == 0:
            g.add_edge(c1,c2)
    else:
        pass
#%%
########### COST GENERATION  
# np.random.seed(5)

costs = []
for i in range(g.size()): 
    costs.append(random.randint(
            sim_setting['min_cost'],
            sim_setting['max_cost'],))


########### RAW MATRIX GENERATION
nodes_matrix_size = (g.order(),g.order())
nodes_matrix = np.zeros(nodes_matrix_size)
for i in range(g.order()):
    for j in range(g.order()):
        if g.has_edge(i,j):
            nodes_matrix[i][j] = 1;
nodes_matrix_triu=np.triu(nodes_matrix, k=0)
    
########### COST ASSIGNMENT

t=0   
for i in range(g.order()):
    for j in range(g.order()):
        if nodes_matrix_triu[i][j] == 1:
            g.edges[i,j]['weight'] = costs[t]
            nodes_matrix[i][j] = costs[t]
            t+=1

            
########### NODES MATRIX 
for i in range(g.order()):
    for j in range(g.order()):
        nodes_matrix [j][i] = nodes_matrix [i][j]
#%%           
   
#         c+=1
# print (g.)    
# pos = nx.circular_layout(g)
# nx.draw(g)
# nx.draw_networkx_edge_labels(g,pos,with_labels=True)
nx.draw_spring(g, with_labels=True)
plt.show()

arc_weight=nx.get_edge_attributes(g,'weight')
print(arc_weight)

print(f"number of nodes: {g.order()}")
print(f"number of edges: {g.size()}")

if nx.is_connected(g):
    print("connected")
else :
    print("not connected")




# #cost assignment
# i = 0
# for node_i in g.nodes():
#     for node_j in g.nodes():
#         if g.has_edge(node_i,node_j) == 1:
#             g.add_weighted_edges_from(node_i,node_j,{costs[i]})
#             i+=1
#         else:
#             pass


