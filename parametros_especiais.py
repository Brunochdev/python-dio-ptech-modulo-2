## Parâmetros Especiais ##


#Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados,
#assim um desenvolvedor precisa apenas olhas para a definição da função para determinar se os itens foram passados:
#por posição
#por nome
#por posição e nome


# Apenas Posição #

def cadastrar_jogo(nome, ano, plataforma,/,estilo, tempo, nota):
    print(nome, ano, plataforma, estilo, tempo, nota)
#tudo que for antes da "/" é obrigatório passar por posição, não pode ser nomeado (nome=algumnome)
#após a barra pode passar dos dois métodos
cadastrar_jogo('Chrono Trigger', 1995, 'Snes', estilo='RPG', tempo=20, nota=10) #Chrono Trigger 1995 Snes RPG 20 10    
#esse método é válido pois está tudo por posição antes da barra, caso nome, ano ou plataforma fosse (ex: ano=1995) daria erro
cadastrar_jogo('Chrono Trigger', 1995, 'Snes', 'RPG', 20, 10) #Chrono Trigger 1995 Snes RPG 20 10
#esse método funciona pq todos os parâmetros foram declarados por posição


# Apenas Nome #

def cadastrar_jogo(*,nome, ano, plataforma, estilo, tempo, nota):
    print(nome, ano, plataforma, estilo, tempo, nota)
#o asterisco indica que tudo será passado apenas por nome
cadastrar_jogo(ano=1995, plataforma='Snes',nome='Chrono Trigger', estilo='RPG', tempo=20, nota=10)   
#esse método é válido pois está tudo por nome, inclusive o "Crono Trigger" que esta "fora de posição"


# Por Posição e Nome #

def cadastrar_jogo(nome, ano, plataforma,/,*,estilo, tempo, nota):
    print(nome, ano, plataforma, estilo, tempo, nota)
#tudo antes da barra é posição, tudo depois do asterisco é por nome
cadastrar_jogo('Chrono Trigger', 1995, 'Snes', estilo='RPG', tempo=40, nota=10)
cadastrar_jogo('Earthbound', 1994, 'Snes', tempo=40, estilo='RPG', nota=10)
#cada caso se encaixa melhor de uma maneira, mas no fim o que importa é a padronização dos dados passados


# Objetos de Primeira Classe #

#Em Python tudo é objeto, inclusive funções, o que as tornam objetos de primeira classe.
#Com isso podemos atribuir funções a variáveis, passa-las como parâmetros para funções, 
#usa-las como valores em estruturas de dados (listas, tuplas, dicionários, etc)
#e usar como valore de retorno para uma função (closures)

def soma(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def conta(a,b):
    return (a*2)+b-5
#declara uma função com dois argumentos que retornam uma soma
def resultado(a, b, nomequalquer):
    resultado = nomequalquer(a, b)
    print(f'O resultado da operação será: {resultado}')
#a função resultado não se importa com o nome real da função passada (nomequalquer) 
#Ela simplesmente executa a função passada como o terceiro argumento, seja qual for o nome dela.
resultado(33, 12, soma)
resultado(33, 12, subtrair)
resultado(33, 12, conta)

resultado_variavel_soma = soma
#variável recebe o valor da função
resultado_variavel_subtrair = subtrair
resultado_variavel_conta = conta
print(f'O resultado da soma será:',resultado_variavel_soma(33,12))
print(f'O resultado da subtração será:',resultado_variavel_subtrair(33,12))
print(f'O resultado da conta será:',resultado_variavel_conta(33,12))


# Escopo Global e Escopo Local #

#Dentro do bloco de uma função, o escopo é local, portanto sua usabilidade e perdida quando o método acaba
#Para usar objetos globais, usamos a palavra reservada "global", que informa ao interpretador que a variável que está
#sendo manipulada dentro do escopo local, é uma variável global (Essa NÂO é uma boa prática)

idade = 35
#variável está fora do escopo nova_idade
def nova_idade(proximo_aniversario):
    global idade
    idade += proximo_aniversario
    return idade
#faz a chamada da variavel global e usa ela dentro do escopo local
print(nova_idade(1))















