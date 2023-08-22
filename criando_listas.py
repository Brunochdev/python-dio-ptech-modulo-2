## Criando Listas ##

# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto #
# Pode-se criar listas com os comandos "list", "range", ou por dentro do colchetes separados por vírgula #
# Como são objetos mutáveis é possível alterar o valor após a criação #

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'LBA']
print(jogos)
#esse é o método mais usado para listas

vazio = []
print(vazio)
#posso declarar uma lista vazia, não necessariamente precisa ter dados

letras=list('Python')
print(letras)
#apesar de parecer que está sendo retornado o valor python, na verdade cada letra é um elemento

numeros = list(range(8))
print(numeros)
#cria um elemento para cada número dentro do "alcance" de 8, ou seja, de 0 a 7, cada um é um elemento

jogo = ['Chrono Trigger', 'RPG', 1995, 14.99, 'Japão', False]
print(jogo)
#todos os elementos passados no código acima são válidos, desde string até float, etc.



# Acesso Direto #

#Lista é uma sequência, portanto podemos acessar seus índices. Inicia em 0 quando queremos valores positivos.
#Quando o valor for negativo, começa em -1
jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'LBA']
print(jogos[0]) #Chrono Trigger
print(jogos[3]) #LBA
print(jogos[-2]) #Earthbound
print(jogos[-3]) #Fallout


# Listas Aninhadas #

#Podemos ter listas que armazenam outras listas. Com isso criando estruturas bidimensionais (tabelas)
#acessando assim indíces de linhas e colunas

matriz = [
    [5, 'b', 9],
    [7, 4, 'a'],
    ['d', 2, 1],
]
print (matriz[0]) #[5, 'b', 9]
print (matriz[-1][-2]) #2
print (matriz[2][1]) #2
print (matriz[-1][2]) #1


# Fatiamento #

#Podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inical e/ou final,
#é possível ainda informar quantas posições o cursor deve pular no acesso


lista = 'Fatiamento'
print (lista[2:]) #tiamento
print (lista[:2]) #Fa
print (lista[1:4]) #ati
print (lista[0:8:2]) #Ftae
print (lista[::]) #Fatiamento
print (lista[::-1]) #otnemaitaF
#lembrando sempre que o final e exclusivo


# Iterar Listas #

#a forma mais comum de iterar listas é através do comando FOR

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


# Compreensão de Listas

#a compreensão de lista oferece uma sintaxe mais curta para criar uma nova lista com base nos valores de uma lista existente,
#ou gerar uma lista nova aplicando alguma modificação dos elementos de uma lista existente


numeros = [1, 5, 65, 98, 84, 32, 17, 19, 4, 33, 21, 168, 257]
pares = []

for number in numeros:
    if number %2 == 0:
        pares.append(number)

print(pares)        
    

numero = [numero for numero in numeros if numero %2 == 0]

print (numero)

#variáveis numero e pares irão retornar os mesmo valores, somente os pares
#no segundo caso o primeiro "numero" dentro do colchetes é o retorno, ou, o que ira compor o que a lista ira gerar
#a segunda parte é a iteração (estrutura for), e antes de retornar o valor, vai checar se o número tem resto 0

num2 = [1, 5, 65, 98, 84, 32, 17, 19, 4, 33, 21, 168, 257]
quadrado = []

for quad in num2:
    quadrado.append(quad**2)

print(quadrado) 

quad2 = [quad2 **2 for quad2 in num2]

print(quad2)

#dois métodos novamente para retornar os mesmos valores (números sendo elevados ao quadrado)

