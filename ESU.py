import copy
import linecache
import sys
import time
import canon


# Begin of the algorithm
# Pick a random vertex of graph and put your
# adjacences in a list for the next step of the 
# algorithm
def enumerateSubgraph():
    used = []
    with open('saida.txt') as graphText:
        for v, _ in enumerate(graphText):
            vExtension = set()
            line = linecache.getline("saida.txt", v+1).split()
            line = [int(x) for x in line]
        
            for v_adj in line:
                if v_adj > v:
                    vExtension.add(v_adj)
            
            global tam_total
            global space
            
            used.append(v)
            tam_total += len(vExtension)
            extendSubgraph([v], vExtension, v, used[:])

            write_subGraphs()


def extendSubgraph(subGraph, vExtension, v, used):
    global space
    global tam_total
    global subGraphs
    global subTotal
    global canonized
    global count_canon
    space.append(tam_total)
    
    # Check if subGraph has size equals to k
    # Sum 1 to the number of subGraphs founded
    if len(subGraph) == k:
        subTotal += 1
        subGraphs.append(subGraph[:])
        
        graph_canon = canon.canon(subGraph[:])
        if graph_canon in canonized:
            ind = canonized.index(graph_canon)
            count_canon[ind] += 1
        else:
            canonized.append(graph_canon)
            count_canon.append(1)
        #print(graph_canon)
        #input()
        return

    # Take a vertex of vExtension and copy all of your
    # adjacences to a new vExtension
    # Try to expand the subGraph with the possibilities
    # founded in vExtension
    while len(vExtension) != 0:
        w = vExtension.pop()
        vExtension2 = copy.deepcopy(vExtension)
        used.append(w)
        used2 = used[:]

        line = linecache.getline("saida.txt", w+1).split()
        line = [int(x) for x in line]

        for u in line:
            if u not in subGraph and u not in used and u > v:
                vExtension2.add(u)
                
        tam_total += len(vExtension2)-1
        subGraph.append(w)

        extendSubgraph(subGraph, vExtension2, v, used2)
        
        tam_total += -len(vExtension2)
        subGraph.pop(-1)


def write_subGraphs():
    with open("analises/subGrafos.txt", "a") as arq:
        global subGraphs
        for sub in subGraphs:
            arq.write(str(sub) + "\n")
    subGraphs = []

#graph, k = readGraph()
k = int(sys.argv[1])
n = int(sys.argv[2])
space = []
tam_total = 0
subTotal = int(0)
subGraphs = []
canonized = []
count_canon = []

execution = time.time()
enumerateSubgraph()

print(subTotal, time.time()-execution)

for i, _ in enumerate(canonized):
    print(canonized[i], " ", count_canon[i])
if(n == 1):
    with open("analises/analise_space.txt", 'a') as arq:
        arq.write(str(k) + "\n")
        for num in space:
            arq.write(str(num) + ",")
        arq.write("\n")


