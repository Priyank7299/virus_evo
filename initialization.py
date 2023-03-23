# imports
import numpy as np
from treelib import Tree, Node
import global_var as var
import random

# functions

# INITIALIZE the starting virus population
def initialize_virus ():
    virus = []
    for i in range(1, var.virus_length):
        virus.append([0]*var.virus_length)

    LP = init_LP()
    print(LP)
    print(new_virus)
    virus.append(LP)
    print(new_virus)

# INITIALIZE the mutation index for virus genome of length n
def mutation_index ():
    # var.virus_length
    mut_index = []
    return mut_index

def init_LP():
    LP = []
    numLP = random.randint(1, 3)
    for i in range(numLP):
        lethal = random.randint(0, 7)
        if lethal not in LP:
            LP.append(lethal)
    return LP

def initialize_virus_tree ():
    pop = []

    for i in range(var.virus_pop_size):
        individual = Tree()
        nodeID = 1
        parent_nodeID = nodeID
        individual.create_node([0] * var.virus_length, nodeID) # root node
        for j in range(var.virus_tree_size):
            nodeID += 1
            individual.create_node([0] * var.virus_length, nodeID, parent=parent_nodeID)
        pop.append(individual)
    return pop
