import networkx as nx
import random

#Função para adicionar os vertices do grafo
def add_vertices():
  with open(caminho,'r') as arq:
    num_vertices = arq.writelines[0]
    for i in  range(0,num_vertices):
      Grafo.add_node(i)

#Função para adicionar as arestas do grafo
def add_arestas():
  with open(caminho,'r') as arq:
    Grafo.add_edge()

caminho = r'D:\israel\UFJF\APA\trabalho-apa\data\graph.txt'
#Cria o grafo
Grafo = nx.Graph()
add_vertices()
add_arestas()




