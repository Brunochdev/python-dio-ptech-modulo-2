## Métodos da classe List ##

# [].append #

#append serve para adicionar novos itens nas listas. Devem ser declarados entre parenteses

lista = []
print (lista)

lista.append(1)
print (lista)

lista.append('Bruno')
print (lista)

lista.append([39, 12, 'Chagas'])
print ('lista 1: ',(lista))

#a cada novo "append", a saída foi adicionando os itens

# [].clear #

#append serve para apagar listas

lista2 = ([39, 12, 'Chagas'])
print ('lista 2: ',lista2) 

lista2.clear()
print ('lista 2: ', lista2)
#foi apagada a lista, mas não a mensagem


# [].copy #

#copy retorna uma lista igual, porém com instância diferente

lista3 = ([35, 10, 'Bruno'])
print ('lista 3: ',lista3)

l3 = lista3.copy()
print ('lista 3b: ',l3)
#apesar de lista3 e l3 terem os mesmos valores, elas não são a mesma coisa
print(id(lista3), id(l3) )
#identificadores diferentes, apesar de ter os mesmos valores

l3[2] = ('Bruno Chagas')

print(l3) #[35, 10, 'Bruno Chagas']
print(lista3) #[35, 10, 'Bruno']
#adicionando elementos diferentes para comprovar que uma não é igual a outra

# [].count #

#copy retorna quantas vezes um determinado objeto aparece na lista

cores = ['vermelho', 'azul', 'verde azul', 'amarelo', 'azul', 'verde', 'azul',1,1,1,1,1]
print (cores.count('azul')) #3
print (cores.count('verde')) #1
print (cores.count('vermelho')) #1
print (cores.count(1)) #5
#quando o nome é composto, não irá retornar se for declarado apenas uma parte da string


# [].extend #

#adiciona listas a uma lista já existente

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound']
print (jogos)

jogos.extend(['Final Fantasy', 'LBA', 'Earthbound']) 
#variável jogos agora contém todos os jogos declarado, inclusive duas vezes earthbound  
print (jogos) #['Chrono Trigger', 'Fallout', 'Earthbound',Final Fantasy', 'LBA', 'Earthbound']
print (jogos[0])
print (jogos[-1])


# [].index #

#retorna a primeira posição (index) do elemento

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']
print (jogos.index('Chrono Trigger')) #0
print (jogos.index('Earthbound')) #2
#não irá retornar as duas posições de earthbound, somente a primeira "2".
#lembrando que são case sensitive


# [].pop #

#linguagem python trabalha com o conceito de pilhas (empilhamento)
#o uso do "pop", trabalha com a ideia de que seria retirado o último item da pilha primeiro até o item inicial

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']

print(jogos.pop()) #Earthbound
print(jogos.pop()) #LBA
#está "regredindo" do último item até o primeiro
print(jogos.pop(2)) 
print(jogos.pop()) 
print(jogos.pop())
print(jogos.pop())



# [].remove #

#remove a primeira ocorrência do elemento alvo

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']

jogos.remove('Earthbound') #irá remover apenas o primeiro "Earthbound"
print(jogos)


# [].reverse #

#espelha a lista (de trás pra frente)

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']

(jogos.reverse())
print(jogos)



# [].sort #

#ordena a lista em ordem alfabética

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']

(jogos.sort())#ordena em ordem alfabética
print(jogos)

(jogos.sort(reverse=True))#reverte a ordem, sendo assim ao contrário da ordem alfabética
print(jogos)

(jogos.sort(key=lambda x:len(x)))#passada uma função anônima para ordenar por tamanho da string
print(jogos)

(jogos.sort(key=lambda x:len(x), reverse=True))#passada uma função anônima para ordenar por tamanho ao contrário da string
print(jogos)


# função len #

#retorna o tamanho da lista

jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']
 
print(len(jogos))#retorna o número 6, que é a quantidade de elementos dentro da lista



# função sorted #


jogos = ['Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound']


print(sorted(jogos, key=lambda x: len(x))) #funciona como o sort, mas aqui é uma função built-in
# função buit-in é uma função da própria linguagem de programação
print(sorted(jogos, key=lambda x: len(x), reverse=True)) #ordena por tamanho ao contrário da string







