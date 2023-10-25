import linecache
import pynauty as nauty
import matplotlib.pyplot as plt 
import networkx as nx 

def create_graph_for_image(graph):
    g = nx.Graph()
    for i in graph:
        g.add_node(i)
    for i in graph:
        print(graph[i])
        for j in graph[i]:
            g.add_edge(i,j)
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    plt.show()


def canon(graph_received):

    graph = {}
    dict_corresp = {}
    for i, j in enumerate(graph_received):
        dict_corresp[j] = i

    for i in graph_received:
        adjacences = linecache.getline("saida.txt", i+1).split()
        adjacences = [int(x) for x in adjacences]
        
        auxiliar = []
        for j in adjacences:
            if j in graph_received:
                auxiliar.append(dict_corresp[j])
        graph[dict_corresp[i]] = auxiliar
    
    #print(graph)

    graph_nauty = nauty.Graph(number_of_vertices=len(graph_received), directed=False, adjacency_dict=graph, vertex_coloring=[])
    '''automorth = True
    for i in canonized:
        if nauty.isomorphic(i, graph_nauty): 
            automorth = False
            break
    '''
    canonized = nauty.canon_label(graph_nauty)
    return canonized

