## Dicionários ##

#Um dicionário é um conjunto não ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância, do dicionário.
#Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separadas por vírgulas.

jogo = {'nome': 'Chrono Trigger', 'ano': 1995}
#declarada uma variável "jogo" que irá receber um dicionário com dois valores sempre em pares (chave + valor)
#no primeiro caso tem uma chave jogo com valor Chrono Trigger e uma chave ano com valor 1995
print(jogo)

jogo = dict(nome='Chrono Trigger', ano=1995)
#funciona como o caso acima, mas ao invés de declarar entre chaves, declara com a classe dict
print(jogo)

jogo['plataforma'] = 'Snes'
#essa declaração é usada quando já se tem um dicionário criado e quer adicionar uma nova chave a ele
print (jogo)


# Acesso aos Dados #


jogo = {'nome': 'Chrono Trigger', 'ano': 1995, 'plataforma': 'Snes'}

print(jogo['nome']) #Chrono Trigger
print(jogo['ano']) #1995
print(jogo['plataforma']) #Snes
#assim como nas listas eles são acessados com uma chamada entre colchetes
jogo['nome'] = 'Sonic'
jogo['ano'] = 1991
jogo['plataforma'] = 'MD'
#acessando a chave e sobreescrevendo o valor
print(jogo['nome']) #Sonic
print(jogo['ano']) #1991
print(jogo['plataforma']) #MD
#agora os valores de cada par foi alterado


# Dicionários Aninhados #

#Dicionários armazenam qualquer tipo de objeto Python como valor, desde que a chave seja imutável (como strings e números).


jogos = {
    'Chrono Trigger': {'ano': 1995, 'plataforma': 'Snes'},
    'Sonic': {'ano': 1991, 'plataforma': 'MD'},
    'Earthbound': {'ano': 1994, 'plataforma': 'Snes'},
    'Fallout': {'ano': 2008, 'plataforma': 'PC'},
    }
#uma espécie de banco de dados para acessar informações de jogos
print(jogos) #retorna todo o "banco de dados"
print(jogos['Earthbound']['ano']) #1994
#esse print irá retornar o valor da segunda chave (ano) dentro da primeira chave (Earthbound)


# Iterar Dicionários #

#nos dicionários, novamente a forma mais comum de percorrer dados é através do comando FOR

for jogo in jogos:
    print(jogo, jogos[jogo])
#retorna jogo por jogo com seus respectivos dados
#passa linha a linha do dicionário, mas não retorna os valores, somente a chave (Chrono Trigger, Sonic, etc)
#para retornar os dados, faz a chamada no print do dicionário (jogos) e entre colchetes qual a chave para iterar (jogo)
for jogo, valor in jogos.items():
    print(jogo, valor)
#esse método retornará a mesma coisa, mas é mais eficiente


