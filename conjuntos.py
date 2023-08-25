## Conjuntos ##

# Criando sets #

#um set é uma coleção que não possui objetos repetidos, é usado para representar conjuntos matemáticos,
# ou eliminar itens duplicados de um iterável
#set não garante a ordem alfabética (ou qualquer ordem) quando as repetições são eliminadas

print (set([1, 2, 3, 1, 5, 4, 3, 2, 5])) #retorna {1, 2, 3, 4, 5}
#foram eliminadas as repetições dos números
print (set('banana')) #retorna {'n', 'a', 'b'}
#foram eliminadas as repetições das letras nas palavras
print(set(('Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound')))
#retorna {'Earthbound', 'Final Fantasy', 'Chrono Trigger', 'LBA', 'Fallout'}
#foi eliminado o elemento "Earthbound repetido"

#quando usado a declaração direto com {} o código ja "seta" e elimina as repetições
jogos = {'Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound'}
print (jogos)


# Acessando os dados #

#conjuntos em Python não suportam indexação nem fatiamento, então é necessário converter para lista


jogos = {'Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound'}
jogos = list(jogos) #jogos que era um conjunto, foi transformado em uma lista 
print (jogos) #acaba que cada vez que executar o print, sua indexação vai ser diferente, ja que quando é lista não tem ordem
print (jogos[0])


# Iterar conjuntos #

#forma mais comum de iterar conjuntos é através do comando FOR


jogos = {'Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound'}
for jogo in jogos: #percorre o código e retorna uma linha pra cada elemento
    print(jogo) 


# Função Enumerate #


jogos = {'Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound'}
for indice, jogo in enumerate(jogos): 
    print(f'{indice}: {jogo}')

jogos = {'Chrono Trigger', 'Fallout', 'Earthbound', 'Final Fantasy', 'LBA', 'Earthbound'}
for bruno, jogo in enumerate(jogos): 
    print(f'{bruno}: {jogo}')
# o retorno das duas funções será a mesma, a palavra índice é somente uma chamada




# Métodos #

#também existem métodos (e específicos) para os conjuntos


# {}.union


jogos_snes = {'Chrono Trigger', 'Earthbound', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
ano = {1995, 1996, 2002, 2008, 2008}
print(jogos_snes.union(jogos_pc, ano))
#une os três conjuntos, mas sempre lembrando que não coloca em ordem e nem repete elementos


# {}.intersection


jogos_snes = {'Chrono Trigger', 'Earthbound', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
print(jogos_snes.intersection(jogos_pc)) #{'Chrono Trigger', 'Final Fantasy 6'}
#retorna apenas elementos que estão presentes nos dois conjuntos


# {}.difference


jogos_snes = {'Chrono Trigger', 'Earthbound', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
print(jogos_snes.difference(jogos_pc)) #{'Earthbound'}
print(jogos_pc.difference(jogos_snes)) #{'Heroes 3', 'Fallout', 'LBA'}
#retorna elementos que não se repetem dos conjuntos alvos


# {}.symmetric_difference


jogos_snes = {'Chrono Trigger', 'Earthbound', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
print(jogos_snes.symmetric_difference(jogos_pc)) #{'LBA', 'Heroes 3', 'Fallout', 'Earthbound'}
print(jogos_pc.symmetric_difference(jogos_snes)) #{'Fallout', 'LBA', 'Heroes 3', 'Earthbound'}
#retorna elementos que não se repetem nos conjuntos alvos


# {}.issubset


jogos_snes = {'Chrono Trigger', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
print(jogos_snes.issubset(jogos_pc)) #True
print(jogos_pc.issubset(jogos_snes)) #False
#retorna True ou False, dependendo se o conjunto está contido no outro


# {}.issuperset


jogos_snes = {'Chrono Trigger', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
print(jogos_snes.issuperset(jogos_pc)) #False
print(jogos_pc.issuperset(jogos_snes)) #True    
#retorna True ou False, dependendo se o conjunto contém outro


# {}.isdisjoint


jogos_snes = {'Chrono Trigger', 'Final Fantasy 6'}
jogos_pc = {'Fallout', 'LBA', 'Heroes 3', 'Chrono Trigger','Final Fantasy 6'}
jogos_x = {'Fallout', 'Heroes 3', 'LBA'}
print(jogos_snes.isdisjoint(jogos_pc)) #False
print(jogos_pc.isdisjoint(jogos_x)) #False   
print(jogos_x.isdisjoint(jogos_snes)) #True  
#retorna True ou False, dependendo se existe ou não intersecção entre os conjuntos


# {}.add


jogos_total = {'Chrono Trigger', 'Final Fantasy 6', 'Fallout', 'Heroes 3', 'LBA'}
print(jogos_total)
jogos_total.add('Earthbound')
print(jogos_total)
jogos_total.add('Pokémon')
print(jogos_total)
#a cada add, um elemento é adicionado ao conjunto
jogos_total.add('Earthbound')
print(jogos_total)
#um elemento que já esxiste, se adicionado será ignorado


# {}.clear


jogos_total = {'Chrono Trigger', 'Final Fantasy 6', 'Fallout', 'Heroes 3', 'LBA'}
jogos_total.clear()
print(jogos_total)
#limpa o conjunto


# {}.copy


jogos_total = {'Chrono Trigger', 'Final Fantasy 6', 'Fallout', 'Heroes 3', 'LBA'}
print(jogos_total)
print(jogos_total.copy())
#copia os elementos do conjunto


# {}.discard


jogos_total = {'Chrono Trigger', 'Final Fantasy 6', 'Fallout', 'Heroes 3', 'LBA'}
print(jogos_total)
jogos_total.discard('LBA')
print(jogos_total)
#discarta o elemento alvo da chamada


# {}.pop


numeros = {1, 2, 3, 4, 5, 6, 7, 8,}
print(numeros)
print(numeros.pop())
print(numeros)
print(numeros.pop())
print(numeros)
print(numeros.pop())
print(numeros)
#apaga o próximo número da sequência 


# {}.remove


numeros = {1, 2, 3, 4, 5, 6, 7, 8,}
print(numeros)
print(numeros.remove(4))
print(numeros)
print(numeros.remove(7))
print(numeros)
#remove o elemento alvo, mas o elmento deve existir no conjunto (um número 12 por exemplo daria erro)


# {}.discard


numeros = {1, 2, 3, 4, 5, 6, 7, 8,}
print(numeros)
print(numeros.discard(4))
print(numeros)
print(numeros.discard(7))
print(numeros)
#remove o elemento alvo e não retorna erro caso o elemento não exista


#função len


jogos_total = {'Chrono Trigger', 'Final Fantasy 6', 'Fallout', 'Heroes 3', 'LBA'}
print(len(jogos_total)) #5
#retorna o tamanho do conjunto


#função in


jogos_total = {'Chrono Trigger', 'Final Fantasy 6', 'Fallout', 'Heroes 3', 'LBA'}
print('pokémon' in (jogos_total)) #False
print('Chrono Trigger' in (jogos_total)) #True
#retorna True ou False, dependendo se o objeto estará ou não dentro do conjunto









