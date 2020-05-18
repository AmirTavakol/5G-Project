# -*- coding: utf-8 -*-
import time
import logging
from pulp import *


class SimpleKnapsack():
    def __init__(self):
        pass

    def solve(
        self, dict_data, time_limit=None,
        gap=None, verbose=False
    ):
        # x ro inja tarif karde , mesle xe masale ma 
        #inja lower bound dade yani x={0,,,} vali upper nadade
        #tooye masale ma ke xe binary e bayad upper 1 behesh bedim
        logging.info("#########")
        items = range(dict_data['n_items'])

        x = LpVariable.dicts(
            "X", items,
            lowBound=0,
            cat=LpInteger
        )
        # LpContinuous

        problem_name = "knapsack"
        
        prob = LpProblem(problem_name, LpMaximize) #dare mige ke az no e maximization e
        #defining OJ
        prob += lpSum([dict_data['profits'][i] * x[i] for i in items]) , "obj_func"
        #defining constraint
        prob += lpSum([dict_data['sizes'][i] * x[i] for i in items]) <= dict_data['max_size'], "max_vol"
        
        #writes LP model, provided by pulp
        prob.writeLP("./logs/{}.lp".format(problem_name))

        msg_val = 1 if verbose else 0
        start = time.time()
        prob.solve(solver=COIN_CMD())
        end = time.time()
        logging.info("\t Status: {}".format(pulp.LpStatus[prob.status]))

        sol = prob.variables()
        of = value(prob.objective)
        comp_time = end - start

        sol_x = [0] * dict_data['n_items']
        for var in sol:
            logging.info("{} {}".format(var.name, var.varValue))
            if "X_" in var.name:
                sol_x[int(var.name.replace("X_", ""))] = abs(var.varValue)
        logging.info("\n\tof: {}\n\tsol:\n{} \n\ttime:{}".format(
            of, sol_x, comp_time)
        )
        logging.info("#########")
        return of, sol_x, comp_time
