# import Matrix_Definition
import numpy as np
import json
import networkx as nx
import random
import matplotlib.pyplot as plt

fp = open("E:/ICT4SS Lessons/semester 2/Operational research/Project_ex/5G-Project/etc/config.json", 'r')
sim_setting = json.load(fp)

class GP_generator(object):
    def __init__(self,G):
        self.g = G #takes graph G as input
    
    #chooses a random source
    def source_selector(self):
        self.source = np.random.choice(self.g.nodes())
        self.g.nodes[self.source]['label'] = "source"
        print('source:', self.source)
      
    #chooses random destinations
    def destination_selector(self):
        #getting number of destinations from user
        self.n_dest= sim_setting['num_destination']
        self.destinations = []
        self.available_nodes =list(self.g.nodes)
        self.available_nodes.remove(self.source)#remaining nodes after having removed the source
        
        # destination generator    
        for i in range(self.n_dest):
            self.dest=np.random.choice(self.available_nodes)
            self.destinations.append(self.dest)
            self.available_nodes.remove(self.dest)
            self.g.nodes[self.dest]['label'] = "destination"
            
        print('destinations:', end=' ')
        print(*self.destinations,sep=",")
        return self.destinations

    
    #plot graph with source and destination
    def plot(self):
        self.node_pos = nx.get_node_attributes(self.g,'pos')
        self.arc_weight = nx.get_edge_attributes(self.g,'weight')
        node_col = []
        for node in range(self.g.order()):
            if node==self.source:
                node_col.append('red')
            elif node in self.destinations:
                node_col.append('yellow')
            else:
                node_col.append('cyan')
        # node_col = ['red' if node==self.source else 'cyan' for node in range(g.order())]
        nx.draw_networkx_nodes(self.g,pos=self.node_pos, node_color= node_col) #draw nodes
        nx.draw_networkx_labels(self.g,pos=self.node_pos) #label nodes
        nx.draw_networkx_edges(self.g,pos=self.node_pos,edge_color= 'red', style = 'dotted')#draw edges
        nx.draw_networkx_edge_labels(self.g,pos=self.node_pos,edge_labels=self.arc_weight)#label edges
        plt.show()
        print(f"number of nodes: {self.g.order()}")
        print(f"number of edges: {self.g.size()}")
        
        
        
        
        
# if __name__ == '__main__':
    # g = nx.Graph()
    # Graph_Generation_run = Graph_Generation(g)
    # Graph_Generation_run.Node_Generator()
    # Graph_Generation_run.Edge_Generator()
    # Graph_Generation_run.Real_Matrix()
    # Graph_Generation_run.Cost_Assignment()
    # # Graph_Generation_run.plot()
    
    # print('\n\n')
    # aa = GP_generator(g)
    # aa.source_selector()
    # aa.destination_selector()
    # aa.plot()


    
