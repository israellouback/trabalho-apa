import networkx as nx
import path
import numpy as np
import matplotlib.pyplot as plt
import plots


def plota_vetor(vet,flag):
  plots.plota_vetor(vet,flag)

def plota_matriz(matriz):
  plots.plota_matriz(matriz)

def plota_grafo():
  nx.draw(Grafo,with_labels=True)
  plt.show()

def soma_uniao(v1,v2):
  vres = []
  i,j =0,0
  while i < len(v1) and j < len(v2):
    if v1[i] < v2[j]:
      vres.append(v1[i])
      i = i + 1
    elif v1[i] > v2[j]:
      vres.append(v2[j])
      j = j + 1
    else:
      vres.append(v1[i])
      i = i + 1
      j = j + 1
  #vres.extend(v1[i:])    
  #vres.extend(v2[j:])
  print(f'Vetor 1: {v1}')  
  print(f'Vetor 2: {v2}')  
  print(f'União dos vetores: {vres}')    
      
def prod_interseccao(v1,v2):
  vres = []
  print(f'Vetor 1: {v1}')  
  print(f'Vetor 2: {v2}')  
  for i in v1:
      if i in v1 and i in v2:
        vres.append(i)

  vres.sort()
  print(f'Interseccao dos vetores: {vres}') 

def imprime_mapeamento_inverso(i,j,k):
  print(f'Dado o índice [{k}] do vetor compactado, a posição correspondente na matriz é: [{i},{j}] '+ '\n')
  print(f'Na posiçao [{k}] do vetor compactado o elemento é {vet_bin[vet_compac[k]]} e na posição [{i},{j}] da matriz, o elemento é {matriz[i][j]} '+ '\n')


def mapeamento_iterativo_inverso(k,N):
  print('|| PROCEDIMENTO ITERATIVO ||'+ '\n')
  i = 0
  indice = vet_compac[k]
  while indice >= (N-i-1):
    indice = indice - (N-i-1)
    i = i + 1
  j = i + indice + 1 
  print(f'i = {i} e j = {j}')
  imprime_mapeamento_inverso(i,j,k)

def mapeamento_inverso():
  print('Função de mapeamento da entrada de um índice k de um vetor para a posição (i,j) da matriz '+ '\n') 
  k = 5000
  print('Digite o índice do vetor para ser mapeado na matriz:' + '\n')
  while(k > len(vet_compac)):
    k = int(input('Digite o índice k:'))

  vetor_binario = np.zeros(TAM)
  vetor_binario = vetcompac_gera_vetbin(vet_compac,vetor_binario)
  indice = vet_compac[k]
  print('|| CALCULO ANALÍTICO ||' + '\n')
  i = 0
  while indice >= (N-i-1):
    indice = indice - (N-i-1)
    i = i + 1
  j = i + indice + 1 
  print(f'i = {i} e j = {j}')
  imprime_mapeamento_inverso(i,j,k)
  mapeamento_iterativo_inverso(k,N)


def imprime_mapeamento(i,j,mapeamento):
  print(f'Dada os índices [{i},{j}] da matriz, a posição correspondente no vetor é [{mapeamento}]'+ '\n')
  print(f'Na posiçao [{i},{j}] da matriz, o elemento é {matriz[i][j]}, e na posição [{mapeamento}] do vetor o elemento é {vet_bin[mapeamento]}'+ '\n')


def mapeamento_recursivo(i,j,N):
  if i == 0:
      return j - i - 1
  else:
      return (N - i - 1 ) + mapeamento_recursivo(i - 1,j,N)
  

def mapeamento_iterativo(i,j,N):
  print('|| PROCEDIMENTO ITERATIVO ||'+ '\n')
  mapea_it = 0
  for k in range(0,i): 
     mapea_it =  mapea_it + (N-k-1)
  mapea_it =  mapea_it + ( j - i - 1)     #Calculo analítico

  imprime_mapeamento(i,j,mapea_it)

def mapeamento_matriz_vetor():
  print('\n'+ 'Função de mapeamento de uma entrada (i,j) da matriz para um índice k de um vetor'+ '\n')  

  print('Digite a entrada da matriz para ser mapeada no vetor:' + '\n')
  i = int(input('Digite o índice i:'))
  j = int(input('Digite o índice j:'))

  print('|| CALCULO ANALÍTICO ||' + '\n')
  ind = 0
  for k in range(0,i): 
    ind = ind + (N-k-1)
  ind = ind + ( j - i - 1)     #Calculo analítico
  print(f' O cálculo analítico para o mapeamento é '+ '\n')
  imprime_mapeamento(i,j,ind)

  mapeamento_iterativo(i,j,N)

  print('|| PROCEDIMENTO RECURSIVO ||'+ '\n')
  mapea_rec = mapeamento_recursivo(i,j,N)
  imprime_mapeamento(i,j,mapea_rec)
  

def vetcompac_gera_vetbin(vet_c,vetor_binario):
  for i in vet_c:
    vetor_binario[i] = 1
  return vetor_binario

def vetor_compacto_gera_matriz():
  print(f'Função de gerar a matriz de adjacencia binária a partir do vetor compactado!' + '\n')
  matriz_adj = np.zeros((N,N))
  vetor_binario = np.zeros(TAM)
  vetor_binario = vetcompac_gera_vetbin(vet_compac,vetor_binario)
  print(vetor_binario)
  i = 0
  j = 1
  for k in vetor_binario: #4950
    matriz_adj[i][j] = k
    matriz_adj[j][i] = k  
    j = j + 1
    if (j == (N)):     
        i = i + 1         
        j = i + 1 
  #plota_matriz(matriz_adj)
  print(matriz_adj)

def matriz_adjacencia_bin(Grafo):
  matriz_adj = np.zeros((N,N))
  for id1 in Grafo.nodes:
    for id2 in Grafo.nodes:
      if Grafo.has_edge(id1,id2):
          matriz_adj[id1 -1 ,id2 - 1] = 1  
  print('Matriz de adj:' +'\n' +f'{matriz_adj}' + '\n')
  plota_matriz(matriz_adj)
  return matriz_adj


def vetor_binario(matriz):
  vetor_bin = []
  for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
      if(j > i):
        vetor_bin.append(matriz[i][j])

  print(f'Vetor binario: {vetor_bin}' + ' \n')
  return vetor_bin   


def vetor_compactado(vetor_binario):
  vet_c = []
  for i in range(len(vetor_binario)):
    if vetor_binario[i] == 1:
      vet_c.append(i)

  print(f'Vetor Compactado: {vet_c}' + ' \n')
  return vet_c    

#Função para adicionar os vertices do grafo
def add_vertices(Grafo,caminho):
  with open(caminho,'r') as arq:
    num_vertices = int(arq.readline().strip())
    for i in range(1,num_vertices + 1):
      Grafo.add_node(i)

#Função para adicionar as arestas do grafo
def add_arestas(Grafo,caminho):
  with open(caminho,'r') as arq:
    for i,linha in enumerate(arq.readlines()):
      if i >=  1:          #ignorar primeira linha (qtd de vertices)
        id1,id2 = linha.split()
        Grafo.add_edge(int(id1),int(id2))


#Cria o grafo
Grafo = nx.Graph()
add_vertices(Grafo,path.caminho1)
add_arestas(Grafo,path.caminho1)
print(f'Grafo criado com {Grafo.number_of_nodes()} vértices e {Grafo.number_of_edges()} arestas!')
plota_grafo()
N = 100    # Numero de vértices ( dimensao da matriz )
TAM = int((N * (N-1) ) / 2)      #Tamanho do vetor binario (parte triangular superior da matriz) 
matriz = matriz_adjacencia_bin(Grafo)
""" vet_bin = vetor_binario(matriz)        #plotar vet bin e vetor compactado ??
vet_compac =  vetor_compactado(vet_bin)
vetor_compacto_gera_matriz()
mapeamento_matriz_vetor()
mapeamento_inverso()
Grafo2 = nx.Graph()s
add_vertices(Grafo2,path.caminho2)
add_arestas(Grafo2,path.caminho2)
print(f'Grafo 2 criado com {Grafo2.number_of_nodes()} vértices e {Grafo2.number_of_edges()} arestas!')
matriz2 = matriz_adjacencia_bin(Grafo2)
vet_bin2 = vetor_binario(matriz2)
vet_compac2 = vetor_compactado(vet_bin2)
soma_uniao(vet_compac,vet_compac2)  
prod_interseccao(vet_compac,vet_compac2) """

#plota_vetor(vet_compac,0)
#plota_vetor(vet_bin,1)














