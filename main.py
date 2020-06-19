#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import logging
import numpy as np
import networkx as nx
from simulator.Matrix_Definition import Graph_Generation
from simulator.group_generator import GP_generator
from simulator.instance import Instance
from solver.Multicast import MultiCast
from heuristic.simpleHeu import SimpleHeu


# np.random.seed(0)


if __name__ == '__main__':
    log_name = "./logs/main.log"
    logging.basicConfig(
        filename=log_name,
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO, datefmt="%H:%M:%S",
        filemode='w'
    )
    
    
    #graph G generation
    G = nx.Graph()
    #graph G configuration
    Graph_Generation_run = Graph_Generation(G)
    Graph_Generation_run.Node_Generator()
    Graph_Generation_run.Edge_Generator()
    Graph_Generation_run.Real_Matrix()
    matrix=Graph_Generation_run.Cost_Assignment()
    # to see raw graph uncomment below line
    # Graph_Generation_run.plot()
    
    #group generator
    #takes configured graph G as input 
    gp1 = GP_generator(G)
    gp1.source_selector()
    gp1.destination_selector()
    gp1.plot()
    
    

    fp = open("./etc/config.json", 'r')
    sim_setting = json.load(fp)
    fp.close()
    # print(sim_setting['total_node'])

    # # inst = Instance(
    # #     sim_setting
    # # )
    # # dict_data = inst.get_data()
    # # print(dict_data)
    prb = MultiCast()
    # aa = MultiCast.aa(G,sim_setting)
    of,sol,sol_f,comp_time,destinations,source,normal_node= prb.solve(
    # of= prb.solve(
        G,
        # sim_setting,
        matrix,
        # verbose=True
        )
    print('\nminimum cost :',of)
    print('chosen edges:', sol)
    print('floats:',sol_f)
    print('computation time:', round(comp_time,5))
''' 
    k = 0
    i = 0
    
    # print(destinations)
    # print(source)
    while i < len(destinations):
      print("\n")
      print("From Source{} to Destination".format(source[0]),destinations[k])
      print(nx.single_source_dijkstra(G,source[0],destinations[k]))
      if i == len(destinations):
          break
      i+=1
      k+=1


    # print(of_exact, sol_exact, comp_time_exact)

    # heu = SimpleHeu(2)
    # of_heu, sol_heu, comp_time_heu = heu.solve(
    #     dict_data
    # )
    # print(of_heu, sol_heu, comp_time_heu)
    
    # # printing results of a file
    # file_output = open(
    #     "./results/exp_general_table.csv",
    #     "w"
    # )
    # file_output.write("method, of, sol, time\n")
    # file_output.write("{}, {}, {}, {}\n".format(
    #     "heu", of_heu, sol_heu, comp_time_heu
    # ))
    # file_output.write("{}, {}, {}, {}\n".format(
    #     "exact", of_exact, sol_exact, comp_time_exact
    # ))
    # file_output.close()
'''    