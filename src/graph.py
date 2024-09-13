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

def matriz_binaria_adjacencia():
  matriz_adjacencia = nx.adjacency_matrix(Grafo).todense()
  matriz_np = np.array(matriz_adjacencia)
  return matriz_np

#Função para adicionar os vertices do grafo
def add_vertices():
  with open(path.caminho,'r') as arq:
    num_vertices = int(arq.readline().strip())
    print(f'num v:{num_vertices}')
    for i in range(1,num_vertices + 1):
      print(i)
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
plota_grafo()
matriz = matriz_binaria_adjacencia()
#plota_matriz()

#n_vertices = Grafo.number_of_nodes()
#n_arestas = Grafo.number_of_edges()
#print(f'number of nodes:{n_vertices} e number of edges:{n_arestas}')












