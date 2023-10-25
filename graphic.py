import numpy as np
import matplotlib.pyplot as plt

arq = ["analise_s.txt", "analise_a.txt", "analise_n.txt", "analise_k.txt"]
label = ["Índice do grafo", "Número de arestas" , "Número de nós", "Tamanho dos subgrafos encontrados", "Número de subgrafos encontrados"]
for i in range(4):
    dados = []
    num_grafos = []
    tem_exec = []
    x = []
    with open("./analises/" + arq[i]) as arquivo:
        num = 0
        tempo = 0
        param = 0
        for index, line in enumerate(arquivo):
            line.rstrip("\n")
            if index%3 == 0:
                aux = (param,num,tempo)
                dados.append(aux)
                param = int(line)
            elif index%3 == 1:
                num = int(line)
            else:
                tempo = float(line)
        dados.append((param,num,tempo))

    dados.pop(0)
    dados = (sorted(dados, key=lambda x: x[0]))
    repeat = 1
    for j in range(1, len(dados)):
        if dados[j][0] == dados[j-1][0]:
            repeat += 1
        else: break
    
    #print(repeat)
    sum_time = 0
    sum_num = 0
    time_ = []
    number_ = []
    for j in range(len(dados)):
        if j%repeat == 0:
            time_.append(sum_time/repeat)
            number_.append(sum_num/repeat)
            sum_time = dados[j][2]
            sum_num = dados[j][1]
        else:
            print(sum_time)
            sum_time += dados[j][2]
            sum_num += dados[j][1]
    time_.append(sum_time/repeat)
    number_.append(sum_num/repeat)
    time_.pop(0)
    number_.pop(0)
    #input()
    fig, (a1,a2) = plt.subplots(1,2)
    match i:
        case 0:
            title = "Número de subgrafos descobertos\n"
            title += "Mesmo algoritmo de geração com os mesmos parametros"
            a1.set_title(title)
            a1.set_xlabel(label[0])
            a2.set_xlabel(label[0])
            number_ = [x[1] for x in dados]
            time_ = [x[2] for x in dados]
            x = np.linspace(1,len(number_),len(number_))
        case 1:
            title = "Subgrafos com mesmo número de nós, mas número diferente de arestas"
            a1.set_title(title)
            a1.set_xlabel(label[1])
            a2.set_xlabel(label[1])
            x = np.linspace(5200, 7000, 10)
        case 2:
            title = "Subgrafos com mesmo número de arestas, mas número de nós diferente"
            a1.set_title(title)
            a1.set_xlabel(label[2])
            a2.set_xlabel(label[2])
            x = np.linspace(1100, 2000, 10)
        case 3:
            title = "Subgrafos encontrados com parametro k diferente"
            a1.set_title(title)
            a1.set_xlabel(label[3])
            a2.set_xlabel(label[3])
            x = [3, 4, 5, 6]
            number_ = [x/1000 for x in number_]
            print(x)
    print(number_)

    #print(len(number_))
    if i != 3:
        a1.set_ylabel(label[4])
    else:
        a1.set_ylabel("Número de subgrafos (em milhares)")
    a1.plot(x, number_)

    a2.set_title("Tempo gasto em cada execução")
    a2.set_ylabel("Tempo em segundos")
    a2.plot(x, time_)
    plt.show()

    input()
'''
with open("./analises/analise_space.txt") as arq:
    num_elements = []
    line2 = 0
    num_k = -1
    fig, axs = plt.subplots(1,4)
    for i, line in enumerate(arq):
        if i % 2 == 0: num_k = int(line)
        else:
            line = line.split(",")
            line.pop(-1)
            line = [int(x) for x in line]
            title = "Espaço gasto encontrando subgrafos de tamanho: " + str(num_k)
            axs[num_k-3].plot(line)
            axs[num_k-3].set_title(title)
            
    plt.tight_layout()
    plt.show()
    
'''

