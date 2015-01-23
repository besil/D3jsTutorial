import networkx as nx
from numpy import genfromtxt
from pprint import pprint

from reader import LineFeed

def read(fname, sep=","):
    fin = open(fname, 'r')
    lines = [ x.strip().split(sep) for x in fin.readlines() ]
    fin.close()
    
    print lines[12]
    split = lines[0]
    header = { split[i]:i for i in range(len(split)) }
    
    return ( header, lines[1:] )
    

if __name__ == '__main__':
    anagr_fname = "../data/anagrafiche.csv"    
    
    header, lines = read(anagr_fname)
    
    lf = LineFeed( header, lines, key=( 'KEY', 0, 1 ) )
    
#     pprint(lf.header)
    
    g = nx.Graph()
    for record in lf:
        sinistro_id = record['SINISTRO'][0]
        ctp         = record['CTP'][0]
        
        cond_nsp    = record[ 'NOM_COND_VEIC_NSP' ][0]
        cond_ctp    = record[ 'NOM_COND_VEIC_CTP' ][0]
        contr_nsp   = record[ 'NOM_CONTR_POL_NSP' ][0]
        test_nsp    = record[ 'NOM_TESTIM_NSP' ][0]
        test_ctp    = record[ 'NOM_TESTIM_CTP' ][0]
        
        contr_nsp   = record[ 'NOM_CONTR_POL_NSP' ][0]
        nom_dann    = record[ 'NOM_DANNEG' ][0]
        
        if contr_nsp != '' and nom_dann != '':
            if not g.has_node(sinistro_id): g.add_node( sinistro_id )
            if not g.has_node(contr_nsp):   g.add_node( contr_nsp   )
            if not g.has_node(nom_dann):    g.add_node( nom_dann    )
            
            node_sinistro   = g[sinistro_id]
            node_contr      = g[contr_nsp]
            node_dann       = g[nom_dann]
            
            
            
    print "Nodes: {}".format(len(g.nodes()))
        
    
#     sinistro = header['SINISTRO']
#     fisc_altro = header['COD_FISC_COND_VEIC_CTP']
#     fisc_nostr = header['COD_FISC_CONTR_POL_NSP']
#     fiscale_altri   = set()
#     fiscali_nstr    = set()
#     
#     for line in lines:
#         fiscale_altri |= { line[fisc_altro] }
#         fiscali_nstr  |= { line[fisc_nostr] }

#     print "Lines:", len(lines)
#     print "Fiscali altri:", len(fiscale_altri)
#     print "Fiscali nostri:", len(fiscali_nstr)
    