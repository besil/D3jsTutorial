#!/usr/bin/python

import json
from networkx.readwrite import json_graph
from pprint import pprint
import random as r

import networkx as nx


fout = "mynetwork/graph.json"

# G = nx.karate_club_graph()


def build_graph():
#     g = nx.Graph()
    
    minNode = 0
    maxNode = 50
    degree = 0.08
    
#     g = nx.erdos_renyi_graph(maxNode, degree);
#     g = nx.powerlaw_cluster_graph(maxNode, 3, 0.2 )
    g = nx.binomial_graph(maxNode, degree)
    weights = { e : r.uniform(0.1, 1.0) for e in g.edges() }
    nx.set_edge_attributes( g, 'weight', weights )
    
    pr = nx.pagerank(g)
    
    def get_attr_for(g, n):
        return {
            "label" : n,
            "index" : n,
            "level" : pr[n],
            "score" : pr[n],
            "links" : g.neighbors(n)
        }
    
    nx.set_node_attributes(g, 'label', { n : n for n in g.nodes() })
    nx.set_node_attributes(g, 'index', { n : n for n in g.nodes() })
    nx.set_node_attributes(g, 'level', { n : 10 for n in g.nodes()})
    nx.set_node_attributes(g, 'score', { n : r.uniform(7, 10) for n in g.nodes() })
    nx.set_node_attributes(g, 'links', { n : g.neighbors(n) for n in g.nodes() })
    
    return g

# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
# for n in g:
#     g.node[n]['name'] = n


# d = json_graph.adjacency_data(g)
# write json


if __name__ == '__main__':
    g = build_graph()
    # write json formatted data
    d = json_graph.node_link_data(g) # node-link format to serialize
    
    json.dump(d, open(fout, 'w'))