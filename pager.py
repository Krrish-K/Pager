# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:06:50 2020

@author: krish
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist(r"page_rank.txt",create_using=nx.DiGraph(),nodetype=int)
nx.draw(G,with_labels=True)
plt.show()