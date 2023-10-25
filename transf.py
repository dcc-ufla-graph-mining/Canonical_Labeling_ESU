import time

file = open("saida.txt", "w")
num = "0"
adjacences = []

with open('smallworld.txt') as graphText:
    for index, line in enumerate(graphText):
        if index <= 3: continue
        #if index == 50: break

        line = line.split("\t")

        if line[0] != num:
            # print(adjacences)
            adjacences.append("\n")
            file.write(" ".join(adjacences))
            num = line[0]
            #adjacences = [num]
            adjacences = [line[1].rstrip("\n")]
        else:
            adjacences.append(line[1].rstrip("\n"))


