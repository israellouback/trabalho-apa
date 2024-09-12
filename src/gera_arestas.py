#Arquivo para gerar arestas aleatoriamentes e salvar no arquivo de leitura do grafo

#Gera K/2 valores aleatorios representando o numero de arestas do Grafo
# Cria uma tupla contendo valores agrupados em em sub_tuplas,
# representando o id dos vertices que possuem arestas
import random

## verifica se ja nao tem aresta entre os 2 vertices, e se os 2 numeros nao sao iguais
# def verifica_adjacencia(arestas):
#    pares_iguais = set()
#    pares_repetidos = set()
#    for i in range(len(arestas)):
#       if arestas[i][0] == arestas[i][1]:
#            pares_iguais.add(arestas[i])

#       for j in range(i+1,len(arestas)):
#          if arestas[i] == arestas[j]:
#             pares_repetidos.add(arestas[i])

#    if pares_iguais or pares_repetidos:

#Função que gera um valor diferente do passado como parâmetro
# Útil nas ocasiões onde há arestas geradas repetidamente e/ou self-loop
def gera_num_diferente(num_repetido):
   num = random.randint(1,num_vertices)

   while num == num_repetido:
      num = random.randint(1,num_vertices)
   return num  

#Função para garantir que não haverá pares de valores (arestas) repetidas   
def verifica_pares_repetidos(valores,num,i):
   num_anterior = valores[i-1]
   par_atual = (num_anterior,num)
   par_atual_reverso = (num,num_anterior)

   for j in range(0,i-2,2):
      if((valores[j],valores[j + 1]) == par_atual or 
         (valores[j + 1],valores[j]) == par_atual or 
         (valores[j],valores[j + 1]) == par_atual_reverso or
         (valores[j + 1],valores[j]) == par_atual_reverso):
         return True
      
   return False   

def gera_numeros(valores):
   for i in range(K):
     if i % 2 == 1: # Gera valor pro índice ímpar
      num = gera_num_diferente(valores[i - 1])
      if i >= 3: 
         while verifica_pares_repetidos(valores, num, i):
            num = gera_num_diferente(valores[i - 1])

     else:  # Índice par
       num = random.randint(1,num_vertices) 

     if i > 0 and valores[i - 1] == num: # Trata se há arestas repetidas
      num = gera_num_diferente(valores[i - 1])
     print(num)
     valores.append(num)

    
            

num_vertices = 8
K = 26
valores = []
gera_numeros(valores)
arestas = tuple((valores[i],valores[i+1]) for i in range(0,len(valores) - 1,2))
print(arestas)
#verifica_adjacencia(arestas)
caminho = r'..\graph.txt'
with open(caminho,"w") as arq:
   arq.writelines(str(num_vertices) + '\n')
   for valor in arestas:
        linha = ' '.join(map(str,valor))
        print(linha)
        arq.writelines(linha + '\n')    

       




