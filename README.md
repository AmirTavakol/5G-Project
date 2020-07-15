# Description
this is the **multicast optimization** project of Operational Research in June/July 2020 implemented in python.
## Requirements to run

In order to successfully run the project requirements are:

1. Python 3.6
2. Pythun pulp library
3. Pythun networkx library
4. Pythun numpy library
5. Pythun time library
6. Pythun json library
7. CBC solver

## Run the project
In order to run the Project, simply run *'main.py'*. To perform modifications of input parameters, refer to *'config.json'* file.

## config.json
inside folder 'etc' there is a json file called *'config.json'* which includes given configuration for the Project. The values are set to those indicted by the Professor Leonardi, however it is possible to edit
     
## Instance Generation
1. Graph generation
   - The base of the problem which is a random graph showing nodes and edges with corresponding costs are created in *'Matrix_Definition.py'* using networkx library and is located inside *simulator* folder
2. Group generation 
   - Set of a source and some destinations is called a group. This is done in *'group_generator.py'* inside *simulator* folder. Each time a sample of *GP_generator* class is generated and its methods are called in *'main.py'*, a new group instance is generated. Therefore this process is iterated up to when desired number of groups are achieved.

## Linear Programming
The exact method to solve the problem is implemented in python using *pulp* library. Decision varibales, Objective function and constraints are defined in *'Multicast.py'* inside *'solver'* folder. In order to find the optimal solution, *CBC solver* is being intorudiced to *pulp*.


## Heuristic method
for heuristic part, we took benefits of Dijkstra's Algortihm. It is for an individual source to one destination so it is not desirable for multicast, yet, by going through 5 steps it becomes suitable for multicast cases. The mentioned algorithm that has been used in our project is based on “Network X”.

1. The first thing it does is to select a group-based node, in other words, choosing a starting node and assign infinity path values to all other nodes.
2. The next step is to find all paths for each source to each destination independently. (Go to each vertex and update its path length)
3. Then, if the path length (cost) of the adjacent vertex is lesser than new path length, don't update it, or if there are any paths containing other destinations as intermediate nodes, simply eliminate them.

Some features of this method outlined below:
Avoid updating path lengths of already visited vertices.
After each iteration, we pick the unvisited vertex with the least path cost.
Repeat until all the vertices have been visited.

4. As a result of above iterative steps, return cost of the shortest path.
5. Eventually, sum all heuristic minimum costs.

