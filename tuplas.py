## Tuplas ##

#tuplas são estruturas muito parecidas com listas, a diferença é que a tupla é imutável

frutas = ('maçã', 'laranja', 'banana', 'abacaxi',)
#para diferenciar uma tupla de uma lista, nesse caso usamos uma virgula ao final do argumento
letras = tuple('Python')
#outra forma de declaração da tupla (não foi necessário a vírgula ao final, já que está chamando pelo comando tuple)
numeros = tuple([1, 17, 65, 42, 31])
#assim como listas a tupla, guarda objetos, e eles podem ser tanto strings, como números, etc
pais = ('Brasil',)
#novamento foi empregado o uso de vírgula ao final do argumento
print(frutas)
print(letras)
print(numeros)
print(pais)


#tupla é uma sequência, e, assim como na lista, podemos acessar os dados através de índices (início em 0 também)


frutas = ('maçã', 'laranja', 'banana', 'abacaxi',)
print (frutas[0]) #maçã
print (frutas[3]) #abacaxi


#suportam indexação negativa (iniciando em -1)


frutas = ('maçã', 'laranja', 'banana', 'abacaxi',)
print (frutas[-1]) #abacaxi
print (frutas[-3]) #laranja


#tuplas aninhadas, criando estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna


matriz = [
    (5, 'b', 9),
    (7, 4, 'a'),
    ('d', 2, 1),
]
print (matriz[0]) #[5, 'b', 9]
print (matriz[-1][-2]) #2
print (matriz[2][1]) #2
print (matriz[-1][2]) #1
#esse seria um caso para garantir que os valores da matriz não fossem alterados


# Fatiamento #

#para extrair um conjunto de valores de uma sequência basta passar o índice inicial e/ou final para acessar o conjunto
#podemos informar ainda quantas posições o cursor deve "pular" (passo) no acesso


lista = 'Fatiamento'
print (lista[2:]) #tiamento
print (lista[:2]) #Fa
print (lista[1:4]) #ati
print (lista[0:8:2]) #Ftae
print (lista[::]) #Fatiamento
print (lista[::-1]) #otnemaitaF
#lembrando sempre que o final e exclusivo


# Iterar Tuplas #

#a forma mais comum de iterar tuplas é através do comando FOR

jogos_lista = ['Chrono Trigger', 'Fallout', 'Earthbound', 'LBA']
for jogo_lista in jogos_lista:
    print(jogo_lista) 
#passa item por item e retorna ao final


# Função Enumerate #

#as vezes é necessário saber qual o índice do objeto dentro do laço for, podemos assim usar enumerate

for indice, jogo_lista in enumerate (jogos_lista):
    print(f'{indice}: {jogo_lista}') 

#retorna uma lista com numeração
#0: Chrono Trigger
#1: Fallout
#2: Earthbound
#3: LBA


#A principal diferença entre tuplas, é que como ela é imutável, existem bem menos métodos para ela


# [].count #

#copy retorna quantas vezes um determinado objeto aparece na tupla

cores = ['vermelho', 'azul', 'verde azul', 'amarelo', 'azul', 'verde', 'azul',1,1,1,1,1]
print (cores.count('azul')) #3
print (cores.count('verde')) #1
print (cores.count('vermelho')) #1
print (cores.count(1)) #5
#quando o nome é composto, não irá retornar se for declarado apenas uma parte da string


# [].index #

#retorna a primeira posição (index) do elemento

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']
print (jogos.index('Chrono Trigger')) #0
print (jogos.index('Earthbound')) #2
#não irá retornar as duas posições de earthbound, somente a primeira "2".
#lembrando que são case sensitive


# função len #

#retorna o tamanho da tupla

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']
 
print(len(jogos))#retorna o número 6, que é a quantidade de elementos dentro da tupla





