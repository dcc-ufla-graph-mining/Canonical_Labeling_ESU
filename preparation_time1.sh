#/bin/bash

preparation(){
    ./graphgen/graphgen -g:e -n:"$1" -m:"$2" -o:smallworld.txt
    rm -r saida.txt
    touch saida.txt
    python transf.py
    clear
    echo "Calculando..."
}
:<<'COM'
# Grafos semelhantes
echo -n "Digite o valor de k, para o qual os algoritimos irão rodar: "
read k
k=$(($k + 0))
result=()
for i in {1..10}; do
    preparation "1000" "5000"
    #result+=$k
    result_aux=()
    result_aux+=($(python3 ESU.py "$k" "0"))
    result+="$k\n"
    result+="${result_aux[0]}\n"
    result+="${result_aux[1]}\n"
done

for elemento in "${result[@]}"; do
    echo -e "$elemento" >> ./analises/analise_s.txt
done
sed -i '$d' ./analises/analise_s.txt
COM

k=4
result=()
preparation "1000" "5000"
clear
echo "Calculando ..."
# Mesmo grafo, diferente k 

for k in {3..6}; do
    result_aux=()
    result_aux+=($(python3 ESU.py "$k" "1"))
    result+="$k\n"
    result+="${result_aux[0]}\n"
    result+="${result_aux[1]}\n"
done

for elemento in "${result[@]}"; do
    echo -e "$elemento" >> ./analises/analise_k.txt
done
sed -i '$d' ./analises/analise_k.txt

:<<'COM'
# Grafos diferentes por arestas
k=4
arestas=5000
result=()
for i in {1..10}; do
    arestas=$((arestas+200))
    preparation "1000" "$arestas"
    result_aux=()
    result_aux+=($(python3 ESU.py "$k" "0"))
    result+="$arestas\n"
    result+="${result_aux[0]}\n"
    result+="${result_aux[1]}\n"
done

for elemento in "${result[@]}"; do
    echo -e "$elemento" >> ./analises/analise_a.txt
done
sed -i '$d' ./analises/analise_a.txt

# Grafos diferentes por nós
k=4
nos=1000
result=()
for i in {1..10}; do
    nos=$((nos+100))
    preparation "$nos" "5000"
    result_aux=()
    result_aux+=($(python3 ESU.py "$k" "0"))
    result+="$nos\n"
    result+="${result_aux[0]}\n"
    result+="${result_aux[1]}\n"
done

for elemento in "${result[@]}"; do
    echo -e "$elemento" >> ./analises/analise_n.txt
done
sed -i '$d' ./analises/analise_n.txt
COM
rm -r smallworld.txt
