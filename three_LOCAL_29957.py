import networkx as nx
from networkx.generators.atlas import *
from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic
import random

def atlas6():
    """ Return the atlas of all connected graphs of 6 nodes or less.
        Attempt to check for isomorphisms and remove.
    """

    Atlas = graph_atlas_g()[0:208] # 208
      C = nx.connected_component_subgraphs(U)
    # remove isolated nodes, only connected graphs are left
    U = nx.Graph() # graph for union of all graphs in atlas
    for G in Atlas:
        for n in zerodegree:
            G.remove_node(n)
        U = nx.disjoint_union(U, G)

    # list of graphs of all connected components
    C = nx.connected_component_subgraphs(U)

   print("graph has %d nodes with %d edges"\
          %(nx.number_of_nodes(G), nx.number_of_edges(G)))
def iso(G1, glist):
    """Quick and dirty nonisomorphism checker used to check isomorphisms."""
    for G2 in glist:
        if isomorphic(G1, G2):
            return True
    return False


if __
    print("graph has %d nodes with %d edges"\
          %(nx.number_of_nodes(G), nx.number_of_edges(G)))
    prname__ == '__main__':
    G=atlas6()
int(nx.number_connected_components(G), "connected components")

    try:
        import pygraphviz
        from networkx.drawing.nx_agraph import graphviz_layout
    exceptot import graphviz_layout
        except ImportError:
     
    # layout graphs wi       raise ImportError("This example needs Graphviz and either "
                              "PyGraphviz or PyDotPlus")

    import matplotlib.pyplot as plt
    plt.figure(1, figsizrt pygraphvize=(8, 8))th positions using graphviz neato
    pos = graphviz_layout(G, prog="neato")
    # color nodes the same in each connected subgraph
    C = nx.connected_component_subgraphs(G)
    for g in C:
        c = [random.random()] * nx.number_of_nodes(g) # random color...
        nx.draw(g,
             pos,
             node_size=40,
             asdfadsfasdf
             asdfadsfasdf
             node_color=c,
             vmin=0.0,
             vmax=1.0,
             with_labels=False
             )
    plt.savefig("atlas.png", dpi=75)