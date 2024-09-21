import networkx as nx
import path
import numpy as np
import matplotlib.pyplot as plt
import plots


def plota_matriz():
  plots.plota_matriz(matriz)

def plota_grafo():
  nx.draw(Grafo,with_labels=True)
  plt.show()

def vetor_compacto_gera_vetor_binario(vet_c):
  N = len(vet_c)
  vetor_binario = np.zeros(N)
  for i in range(len(vet_c)):
    vetor_binario[i] = 1

  return vetor_binario




def vetor_gera_matriz(vet_c):
  N = len(vet_c)
  matriz_adj = np.zeros((N,N))




  return matriz_adj

def matriz_adjacencia_bin():
  matriz_adj = np.zeros((100,100))
  for id1 in Grafo.nodes:
    for id2 in Grafo.nodes:
      if Grafo.has_edge(id1,id2):
          matriz_adj[id1 -1 ,id2 - 1] = 1  
  return matriz_adj


def vetor_binario(matriz):
  vetor_bin = []
  for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
      if(j > i):
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
matriz = matriz_adjacencia_bin()
vet_bin = vetor_binario(matriz)
vet_compac =  vetor_compactado(vet_bin)
#plots.plota_matriz(matriz)













