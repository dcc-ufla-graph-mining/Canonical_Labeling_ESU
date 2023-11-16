import linecache
import pynauty as nauty
import matplotlib.pyplot as plt 
import networkx as nx 


def create_graph_for_image(graph):
    g = nx.Graph()
    for i in graph:
        g.add_node(i)
    for i in graph:
        for j in graph[i]:
            g.add_edge(i,j)
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    plt.show()

def non_canonical_graph(canon_label_esp, graph):
    new_graph = {}
    for i, _ in enumerate(graph):
        new_graph[i] = []

    for i in graph:
        for j in graph[i]:
            new_graph[canon_label_esp[i]].append(canon_label_esp[j])
        
    return new_graph

def canonical_graph(canon_label, graph):
    new_graph = {}
    for key, value in graph.items():
        index_ = canon_label.index(key)
        new_graph[index_] = []
        for i in value:
            new_graph[index_].append(canon_label.index(i))
        new_graph[index_].sort()

    return new_graph



def canon(graph_received):
    graph = {}
    dict_corresp = {}
    for i, j in enumerate(graph_received):
        graph[j] = []
        dict_corresp[j] = i

    for i in graph_received:
        adjacences = linecache.getline("saida.txt", i+1).split()
        adjacences = [int(x) for x in adjacences]
        
        for j in adjacences:
            if j in graph_received:
                graph[i].append(j)
                graph[j].append(i)

    graph = non_canonical_graph(dict_corresp, graph)
    

    graph_nauty = nauty.Graph(number_of_vertices=len(graph_received), directed=False, adjacency_dict=graph, vertex_coloring=[])

    canonized = nauty.canon_label(graph_nauty)
    new_graph = canonical_graph(canonized, graph)


    return canonized, new_graph, graph
