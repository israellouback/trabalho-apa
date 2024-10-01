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


def imprime_mapeamento_inverso(i,j,k):
  print(f'Dado o índice {k} do vetor, a posição correspondente na matriz é: {i},{j} '+ '\n')
  print(f'Na posiçao {k} do vetor o elemento é {vet_bin[k]} e na posição {i},{j} da matriz, o elemento é {matriz[i][j]} '+ '\n')


def mapeamento_iterativo_inverso(k,N):
  print('|| PROCEDIMENTO ITERATIVO ||'+ '\n')
  i = int(k / N)
  j = k % N
  imprime_mapeamento_inverso(i,j,k)


def mapeamento_inverso(k):
  print('Função de mapeamento da entrada de um índice k de um vetor para a posição (i,j) da matriz '+ '\n') 
  vetor_binario = np.zeros(TAM)
  vetor_binario = vetcompac_gera_vetbin(vet_compac,vetor_binario)
  print('|| CALCULO ANALÍTICO ||' + '\n')
  i = int(k / N)
  j = k % N
  print(f'i = {i} e j = {j}')
  imprime_mapeamento_inverso(i,j,k)
  mapeamento_iterativo_inverso(k,N)


def imprime_mapeamento(i,j,mapeamento):
  print(f'Dada os índices {i},{j} da matriz, a posição correspondente no vetor é {mapeamento}'+ '\n')
  print(f'Na posiçao {i},{j} da matriz, o elemento é {matriz[i][j]}, e na posição {mapeamento} do vetor o elemento é {vet_bin[mapeamento]}'+ '\n')


def mapeamento_recursivo(i,j,N):
  if j == 0:
      return i*N
  else:
      return mapeamento_recursivo(i,j - 1, N) + 1
  

def mapeamento_iterativo(i,j,N):
  print('|| PROCEDIMENTO ITERATIVO ||'+ '\n')
  mapea_it = (i * N) + j
  imprime_mapeamento(i,j,mapea_it)

 

def mapeamento_matriz_vetor(i,j):
  print('Função de mapeamento de uma entrada (i,j) da matriz para um índice k de um vetor'+ '\n')  

  print('|| CALCULO ANALÍTICO ||' + '\n')
  k = (i * N) + j     #Calculo analítico
  print(f' O cálculo analítico para o mapeamento é  k = i * N + j'+ '\n')
  imprime_mapeamento(i,j,k)

  mapeamento_iterativo(i,j,N)

  print('|| PROCEDIMENTO RECURSIVO ||'+ '\n')
  mapea_rec = mapeamento_recursivo(i,j,N)
  imprime_mapeamento(i,j,mapea_rec)
  

def vetcompac_gera_vetbin(vet_c,vetor_binario):
  for i in range(len(vet_c)):
    vetor_binario[i] = 1
  return vetor_binario

def vetor_compacto_gera_matriz():
  matriz_adj = np.zeros((N,N))
  vetor_binario = np.zeros(TAM)
  vetor_binario = vetcompac_gera_vetbin(vet_compac,vetor_binario)
  i = 0
  j = 0
  for k in range(TAM): #4950
    matriz_adj[i][j] = vetor_binario[k] 
    j = j + 1
    if (j == (N-1)):     # N OU N-1
      i = i + 1         
      j = i  
  #plota_matriz(matriz_adj)

def matriz_adjacencia_bin():
  matriz_adj = np.zeros((N,N))
  for id1 in Grafo.nodes:
    for id2 in Grafo.nodes:
      if Grafo.has_edge(id1,id2):
          matriz_adj[id1 -1 ,id2 - 1] = 1  
  return matriz_adj


def vetor_binario(matriz):
  vetor_bin = []
  for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
      if(j >= i):
        vetor_bin.append(matriz[i][j])

  return vetor_bin   


def vetor_compactado(vetor_binario):
  vet_c = []
  for i in range(len(vetor_binario)):
    if vetor_binario[i] == 1:
      vet_c.append(i)

  return vet_c    

#Função para adicionar os vertices do grafo
def add_vertices():
  with open(path.caminho,'r') as arq:
    num_vertices = int(arq.readline().strip())
    for i in range(1,num_vertices + 1):
      Grafo.add_node(i)

#Função para adicionar as arestas do grafo
def add_arestas():
  with open(path.caminho,'r') as arq:
    for i,linha in enumerate(arq.readlines()):
      if i >=  1:          #ignorar primeira linha (qtd de vertices)
        id1,id2 = linha.split()
        Grafo.add_edge(int(id1),int(id2))


#Cria o grafo
Grafo = nx.Graph()
add_vertices()
add_arestas()
print(f'Grafo criado com {Grafo.number_of_nodes()} vértices e {Grafo.number_of_edges()} arestas!')
#plota_grafo()
N = 6     # Numero de vértices ( dimensao da matriz )
TAM = int((N * (N-1) ) / 2)      #Tamanho da parte triangular superior da matriz 
matriz = matriz_adjacencia_bin()
#plota_matriz(matriz)
print(f'Matriz de adj:  + \n')
print(f'{matriz} +\n' )
vet_bin = vetor_binario(matriz) #plotar vet bin e vetor compactado
print(f'Vetor binario: {vet_bin}' + ' \n')
vet_compac =  vetor_compactado(vet_bin)
print(f'Vetor Compactado: {vet_compac}' + ' \n')
vetor_compacto_gera_matriz()
print('Digite a entrada da matriz para ser mapeada no vetor:' + '\n')
i = int(input('Digite o índice i:'))
j = int(input('Digite o índice j:'))
mapeamento_matriz_vetor(i,j)
print('Digite o índice do vetor para ser mapeado na matriz:' + '\n')
k = int(input('Digite o índice k:'))
mapeamento_inverso(k)


#plota_vetor(vet_compac,0)
#plota_vetor(vet_bin,1)














