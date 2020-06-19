# -*- coding: utf-8 -*-
import time
import logging
from pulp import *
import networkx as nx

class MultiCast():
    def __init__(self):
        pass
    def solve(
        self, G, 
        # simple_data,
        matrix
        # time_limit=None,
        # gap=None, verbose=False
        ):  
        destinations = []
        source =[]
        normal_nodes = [i for i in G.nodes]
        all_nodes = [i for i in G.nodes]
        # normal_nodes = range(G.order())
        s_d = nx.get_node_attributes(G,"label")
        for key in s_d.keys():
            if s_d[key] == 'destination':
                destinations.append(key)
                normal_nodes.remove(key)
            elif s_d[key] == 'source':
                source.append(key)
                normal_nodes.remove(key)
            else:
                pass
         
        weight = nx.get_edge_attributes(G,'weight')
        # print(destinations)
        # print(source)
        # print(normal_nodes)
        
        # x ro inja tarif karde , mesle xe masale ma 
        #inja lower bound dade yani x={0,,,} vali upper nadade
        #tooye masale ma ke xe binary e bayad upper 1 behesh bedim
        logging.info("#########")
        # items = range(dict_data['n_items'])
        
        # V = LpVariable(
        #     G.order(),
        #     cat=LpInteger
        #     )
        # E = LpVariable(
        #     G.size(),
        #     cat=LpInteger
        #     )
        # D = LpVariable.dicts(
        #     'D',((destinations[i]) for i in range(len(destinations))),
        #     cat=LpInteger
        # )
        ##
        n_nodes = range(G.order())
        # times = range(G.order())
        
        # xe = LpVariable.dicts( #?
        #     "X", (n_nodes,n_nodes),
        #     lowBound=0,
        #     upBound=1,
        #     cat='Binary'
        #     )
        xe = LpVariable.dicts( #?
            "X", [(i,j) for i in n_nodes for j in n_nodes],
            lowBound=0,
            upBound=1,
            cat=LpBinary
            )
        f = LpVariable.dicts( #?
            "F",[(i,j) for i in n_nodes for j in n_nodes],
            lowBound=0,
            upBound=int(len(destinations)),
            cat=LpInteger
            )
        
        # return V,E,D,xe,f_ij
        # return xe
      
        # LpContinuous

        problem_name = "MultiCast"
        
        prob = LpProblem(problem_name, LpMinimize)
        # #defining OJ
        prob += lpSum([matrix[i][j] * xe[(i,j)] for i in n_nodes for j in n_nodes]) , "obj_func"
        
        #defining constraint       
        ############ constraint 1 on Formula ############
        for i in normal_nodes:
            prob += lpSum([f[(i,j)] for j in n_nodes if matrix[i][j]])-lpSum([f[(k,i)] for k in n_nodes if matrix[k][i]]) == 0, 'flow balance for node{}'.format(i)
         
        ############ constraint 4 on Formula ############
        ex_dest = normal_nodes+source
        for i in all_nodes:
            for j in all_nodes:
            # for j in ex_dest:
                 if matrix[i][j]:
                    prob += f[(i,j)] <= (len(destinations)*xe[(i,j)]) 
                    
        ############ constraint 2 on Formula ############ 
        prob += lpSum([f[(source[0],j)] for j in n_nodes if matrix[source[0]][j]]) == len(destinations), 'output flow from source'
        
        ############ constraint 3 on Formula ############ 
        for d in destinations:
            prob += lpSum([f[(i,d)] for i in n_nodes if matrix[i][d]]) == 1 ,'input flow to destination {}'.format(d)
        ############ constraint new on Formula ############
        prob += lpSum([f[(i,source[0])] for i in n_nodes if matrix[i][source[0]]]) == 0, 'no input to source'
        #writes LP model, provided by pulp
        prob.writeLP("E:/ICT4SS Lessons/semester 2/Operational research/Project_ex/5G-Project/logs/{}.lp".format(problem_name))

        # msg_val = 1 if verbose else 0
        start = time.time()
        prob.solve(solver=COIN_CMD())
        end = time.time()
        logging.info("\t Status: {}".format(pulp.LpStatus[prob.status]))
        # print(pulp.LpStatus[prob.status])

        sol = prob.variables()
        of = value(prob.objective)
        comp_time = end - start
        
        sol_x = []
        sol_f = []
        for var in sol:
            logging.info("{} {}".format(var.name, var.varValue))
            x_name = var.name
            x_value =  var.varValue
            if "X_" in var.name:
                if x_value != 0:
                    sol_x.append(var.name.replace("X_", ""))
            if "F_" in var.name:
                if x_value !=0:
                    sol_f.append((var.name.replace("F_", ""),var.varValue))
        logging.info("\n\tof: {}\n\tsol:\n{} \n\ttime:{}".format(of, sol_x, comp_time))
        logging.info("#########")
        
        return of,sol_x,sol_f,comp_time,destinations,source,normal_nodes
