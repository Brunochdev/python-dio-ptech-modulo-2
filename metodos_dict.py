## Métodos Dicionário##




# {}.clear #

#apaga todos os valores do dicionário

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }

jogos.clear()
print(jogos) #{}


# {}.copy #

#faz uma cópia do dicionário

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'}
    }
copia = jogos.copy() #cópia com novo nome
print(copia)
copia['Chrono Trigger'] = {'ano': 2023, 'plataforma': 'Snes', 'estilo': 'RPG'}
print(jogos)
print(copia) #pode inclusive adicionar dados


# {}.fromkeys #

#cria chaves em duas situações

print(dict.fromkeys(['estilo', 'musica'])) #{'estilo': None, 'musica': None}
#criou duas chaves vazias
print(dict.fromkeys(['estilo', 'musica'],'vazio')) #{'estilo': 'vazio', 'musica': 'vazio'}
#criou duas chaves com valores setados para "vazio"
#pode ser um dicionário existente ou não


# {}.get #

#outra forma de acessar valores dentro de um dicionário, quando não se sabe se uma chave existe ou não

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'}
    }

print(jogos.get('Earthbound')) #none
#como a chave estilo não existe, o retorno será none
print(jogos.get('Earthbound','não existe')) #{'não existe'}
#é possível passar um retorno "default", como nesse caso que foi usado o "alerta": "não existe", caso não seja encontrado
print(jogos.get('Chrono Trigger','não existe')) #{'ano': 1995, 'plataforma': 'Snes'}
#como o valor é existente, não irá retornar "{não existe}"


# {}.items #

#retorna uma lista de tuplas, muito importante para comandos FOR

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }

print(jogos.items()) #dict_items([('Chrono Trigger', {'ano': 1995, 'plataforma': 'Snes'}), ('Sonic', {'ano': 1991,...etc...])
#retorna todos os itens do dicionário, chaves, nomes, etc


# {}.keys #

#retorna somente as chaves do dicionário

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }

print(jogos.keys()) #dict_keys(['Chrono Trigger', 'Sonic', 'Earthbound', 'Fallout'])


# {}.pop #

#remove e retorna o valor que removeu

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }
print(jogos.pop('Fallout')) #foi excluído os dados de Fallout 
print(jogos.pop('Sonic')) #foi excluído os dados de Sonic 
print(jogos) 
#agora retorna {'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'}, 'Earthbound': {'ano': 1994, 'plataforma': 'Snes'}}
print(jogos.pop('Sonic','jogo não encontrado'))
#assim como o get, ele consegue retornar um valor/aviso caso a chave não seja encontrada


# {}.popitem #

#retira os itens na sequência, sem a necessidade de informar a chave

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }
print(jogos.popitem()) #foi excluído os dados de Fallout 
print(jogos)


# {}.setdefault #

#muito usado, pois se o atributo não estiver no dicionário, irá ser adicionado com o valor informado,
#caso o atributo exista, irá retornar o valor existente e não fara a alteração

jogos = {'Nome': 'Chrono Trigger', 'ano': 1995, 'plataforma': 'Snes'}
print(jogos.setdefault('plataforma', 'MD'))
print(jogos) #retornou Snes e não MD pq o valor não se altera
print(jogos.setdefault('estilo', 'RPG'))
print(jogos) #já quando é inserida uma informação que não estava contida, ela retorna sendo adicionada as demais


# {}.update #

#atualiza as informações de um dicionário com informações vindo de outro dicionário

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    }
print(jogos)
jogos.update({
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
})
print(jogos)
#o segundo print irá conter todas as informações contidas nos dois dicionários
jogos.update({'Sonic':{'plataforma': 'Mega Drive'}})
print(jogos)
#na hora do print todo o conteúdo será trocado por apenas 'Sonic': {'plataforma': 'Mega Drive'}
jogos.update({'Sonic': {'ano': 1991, 'plataforma': 'Mega Drive'}})
print(jogos) #'Sonic': {'ano': 1991, 'plataforma': 'Mega Drive'}
#agora sim segue as informações padronizadas e todo o conteúdo é exibido


# {}.values #

#retorna somente os dados da chave

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }

print(jogos.values())
#diferente do keys, nesse caso irá retornar os dados {'ano': 1995, 'plataforma': 'Snes'}...etc...


# in #

#método mais elegante para saber se uma chave existe ou não

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }

print ('Chrono Trigger' in jogos) #True
print ('Chrono ' in jogos) #False
print ('ano' in jogos['Chrono Trigger']) #True
#retorna mesmo em casos onde existe uma chave (ano) dentro de uma chave (Chrono Trigger)
print ('ano' in jogos) #False
print ('Earthbound' in jogos) #True


# del #

#deleta um elemento

jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }

print(jogos)

del jogos['Sonic']['ano']
print(jogos) #irá retornar a chave Sonic com apenas a chave interna plataforma e seu dado MD

del jogos['Fallout']
print(jogos) #retorna com delete completo da chave Fallout + o delete prévio do ano de Sonic
