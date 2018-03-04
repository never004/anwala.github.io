import networkx as nx
from matplotlib import pylab as plab
from operator import itemgetter

def removeEdge(G):
    dic1 = nx.edge_betweenness_centrality(G)
    tupleList = dic1.items()
    tupleList = sorted(tupleList,key=lambda x:x[1], reverse=True)
    for x in tupleList:
        return x[0]
def girvanNewman(G):
    c = nx.connected_component_subgraphs(G)
    l = len(list(c))
    pos = nx.spring_layout(G)
    count = 0
    print(count, "Connected components: ", l)
    op = "karate%(id)02d.png" % {"id": count}
    plab.figure()
    nx.draw_networkx(G, pos)
    plab.savefig(op)
    plab.close()
    while(l < 3): # loop stops at l = 3
        G.remove_edge(*removeEdge(G))
        c = nx.connected_component_subgraphs(G)
        l = len(list(c))
        pos = nx.spring_layout(G)
        count += 1
        print(count, "Connected components: ", l)
        op = "karate%(id)02d.png" % {"id": count}
        plab.figure()
        nx.draw_networkx(G, pos)
        plab.savefig(op)
        plab.close()
    return c
G = nx.karate_club_graph()
c = girvanNewman(G)
