import networkx as nx
from matplotlib import pylab as plab
from operator import itemgetter

def removeEdge(G):
    dic1 = nx.edge_betweenness_centrality(G) # edge_betweenness_centrality a major nx function
    tupleList = dic1.items() # also we need a dictionary for the items
    #tupleList.sort(key=itemgetter(0))
    #tupleList.sort(key=itemgetter(1), reverse=True) #testing lines for sorting
    tupleList = sorted(tupleList,key=lambda x:x[1], reverse=True) # need to save this into a new tupleList
    #print(dict1)
    #print(tupleList)
    for x in tupleList:
        #print(x[0]), test line
        return x[0]
    #sorted(tupleList())
    #return tupleList[0][0] #(a,b) # more testing lines, for sort and return
def girvanNewman(G): # algorithm
    c = nx.connected_component_subgraphs(G)
    l = len(list(c))
    pos = nx.spring_layout(G)
    count = 0 # count initialized for loop later on
    print(count, "Connected components: ", l) # this is the first iteration
    op = "karate%(id)02d.png" % {"id": count} # the loop contains more comments here
    plab.figure()
    nx.draw_networkx(G, pos)
    plab.savefig(op)
    plab.close()
    while(l == 1): #loop is the same as the code before but STOPS after the graph splits into two (l = 2)
        #print(removeEdge(G)) # test line
        G.remove_edge(*removeEdge(G)) #((a,b)) -> (a,b) # remove ambig ()
        c = nx.connected_component_subgraphs(G)
        l = len(list(c)) # l will be the length of the list, naturally
        pos = nx.spring_layout(G)
        count += 1 # increment count
        print(count, "Connected components: ", l) #prints # of connected components to console as well as iterations
        op = "karate%(id)02d.png" % {"id": count} # output files will be karate00.png, karate01.png, etc.
        plab.figure()
        nx.draw_networkx(G, pos) #draws the graphs
        plab.savefig(op) # save
        plab.close() # and close
    return c
G = nx.karate_club_graph()
c = girvanNewman(G)
