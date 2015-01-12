#!/usr/bin/python

import json
import networkx as nx
from networkx.readwrite import json_graph
from pprint import pprint

fout = "mynetwork/graph.json"

# G = nx.karate_club_graph()
G = nx.barabasi_albert_graph(10, 2);

# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
# for n in G:
#     G.node[n]['name'] = n

# write json formatted data
d = json_graph.node_link_data(G) # node-link format to serialize
# d = json_graph.adjacency_data(G)
# write json

json.dump(d, open(fout,'w'))
