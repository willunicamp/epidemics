#!/usr/bin/env python

__author__ = "William Roberto de Paiva"
__license__ = "GPL"
__maintainer__ = "William Roberto de Paiva"
__email__ = "will.unicamp@gmail.com"
__status__ = "Production"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def Initialize():
	#generate graph
	G = nx.barabasi_albert_graph(1000,5)
	#create figure space	
	plt.figure(figsize=(8,8))
	pos=nx.spring_layout(G)
	#start epidemics definitions
	n = nx.number_of_nodes(G)
	p = 0.01
	infected = np.zeros(n)
	infected[50] = 1
	#start simulation
	for i in range(1000):
		plt.clf()
		for node in G.nodes():
			if(infected[node] == 1):
				for neighbor in G.neighbors(node):
					infect = random.random()
					if(infect <= p):
						infected[neighbor] = 1
		nx.draw(G,pos=pos, node_color=infected, node_size=40)
		plt.savefig("teste"+format(i, '04d')+".png")

	
	

if __name__ == "__main__":
    Initialize()
