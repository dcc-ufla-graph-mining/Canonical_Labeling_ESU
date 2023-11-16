import canon
import ESU

def receive_graph(subGraph):
    #print(subGraph)
    global label, count_canon, canonized, not_canonized
    subGraph = subGraph[:]
    graph_canon_label, graph_canon, graph_noncanon = canon.canon(subGraph)

    if graph_canon not in canonized:
        canonized.append(graph_canon)
        not_canonized.append(graph_noncanon)
        
        canon.create_graph_for_image(graph_canon)

    if graph_canon_label in label:
        count_canon[label.index(graph_canon_label)] += 1
    else:
        count_canon.append(1)
        label.append(graph_canon_label)




def main():
    subGraphs = ESU.main()
    #print(subGraphs)
    for i in subGraphs:
        receive_graph(i)

canonized = []
not_canonized = []
label = []
count_canon = []
main()
