import networkx as nx
from numpy import genfromtxt
from pprint import pprint

from reader import LineFeed

def read(fname, sep=","):
    fin = open(fname, 'r')
    lines = [ x.strip().split(sep) for x in fin.readlines() ]
    fin.close()
    
    split = lines[0]
    header = { split[i]:i for i in range(len(split)) }
    
    return ( header, lines[1:] )
    

if __name__ == '__main__':
    anagr_fname = "../data/anagrafiche.csv"    
    
    data = read( anagr_fname, sep="," )
    header, lines = read(anagr_fname)
    
    lf = LineFeed( header, lines )
    
    g = nx.Graph()
    for l in lf:
        sinistro_id = l['SINISTRO']
        g.add_node(sinistro_id, attr_dict)
    
#     sinistro = header['SINISTRO']
#     fisc_altro = header['COD_FISC_COND_VEIC_CTP']
#     fisc_nostr = header['COD_FISC_CONTR_POL_NSP']
#     fiscale_altri   = set()
#     fiscali_nstr    = set()
#     
#     for line in lines:
#         fiscale_altri |= { line[fisc_altro] }
#         fiscali_nstr  |= { line[fisc_nostr] }
    
    print "Lines:", len(lines)
    print "Fiscali altri:", len(fiscale_altri)
    print "Fiscali nostri:", len(fiscali_nstr)
    