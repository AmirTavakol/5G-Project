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
...
