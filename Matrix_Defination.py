import numpy as np
import json
import networkx as nx
import random
import matplotlib.pyplot as plt

fp = open("./etc/config.json", 'r')
sim_setting = json.load(fp)
print(sim_setting)


class Graph_Generation():
    def __init__(self, g):
        self.g = g

    def Node_Generation(self):
        pass

    def Edge_Generator(self):
        c1 = np.random.choice(g.nodes())
        c2 = np.random.choice(g.nodes())
        if c1 != c2 and g.has_edge(c1, c2) == 0:
            g.add_edge(c1, c2)
        for j in (range(sim_setting["total_node"])):
            while (g.degree(j) <= 1):
                c1 = np.random.choice(g.nodes())
                c2 = np.random.choice(g.nodes())
                if c1 != c2 and g.has_edge(c1, c2) == 0:
                    g.add_edge(c1, c2)
            else:
                pass

    def Real_Matrix(self):
        costs = []
        for i in range(g.size()):
            costs.append(random.randint(
                sim_setting['min_cost'],
                sim_setting['max_cost'],))
        nodes_matrix_size = (g.order(), g.order())
        nodes_matrix = np.zeros(nodes_matrix_size)
        for i in range(g.order()):
            for j in range(g.order()):
                if g.has_edge(i, j):
                    nodes_matrix[i][j] = 1
        nodes_matrix_triu = np.triu(nodes_matrix, k=0)
        print(nodes_matrix_triu)
        t = 0
        for i in range(g.order()):
            for j in range(g.order()):
                if nodes_matrix_triu[i][j] == 1:
                    g.edges[i, j]['weight'] = costs[t]
                    nodes_matrix[i][j] = costs[t]
                    t += 1
        for i in range(g.order()):
            for j in range(g.order()):
                nodes_matrix[j][i] = nodes_matrix[i][j]

    def plot(self):
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


g = nx.Graph()
for i in (range(sim_setting["total_node"])):
    nodes = g.add_node(i)

if __name__ == '__main__':
    Graph_Generation_run = Graph_Generation(g)
    Graph_Generation_run.Node_Generation()
    Graph_Generation_run.Edge_Generator()
    Graph_Generation_run.Real_Matrix()
    Graph_Generation_run.plot()
