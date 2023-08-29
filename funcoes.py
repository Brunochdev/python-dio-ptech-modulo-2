## Funções ##


#O uso de funções torna o código mais legível, além de possibilitar reaproveitamento.
#Programar baseado em funções é o mesmo que dizer que estamos programando de maneira estruturada.
#Uma função é um bloco de códigos identificado por um nome e pode receber uma lista de parâmetros. 
#Os parâmetros podem ou não ter valores padrões.
#Tem um conjunto de entrada e de saída


# def #

#para mostrarmos ao interpretador que usaremos uma função, usa-se a palavra reservada "def"

def exibir_msg():
    print('Bem vindo ao aprendizado de funções!! \n')
    
def exibir_msg_2(nome):
    print(f'Bem vindo {nome}!! \n')

def exibir_msg_3(nome='Bruno'):
    print(f'Bem vindo {nome}!! \n')
#todos esses métodos foram apenas para declarar as funções e não para executa-las, ou seja, nada será impresso em tela


exibir_msg() #Bem vindo ao aprendizado de funções!!
#nesse momento a função está sendo chamada para executa-la, e assim, exibir em tela o texto
exibir_msg_2(nome='Bruno') #Bem vindo Bruno!!
#novamente houve a chamada para execução, e dessa vez com a inclusão de um argumento vazio para nome
#sempre que houver um argumento não declarado, é necessário passar algum parâmetro
exibir_msg_3() #Bem vindo Bruno!!
#como o nome Bruno já havia sido declarado em função, bastou fazer sua chamada
exibir_msg_3(nome='Pedro') #Bem vindo Pedro!!
#mesmo com o argumento para nome declarado em função, foi possível fazer sua alteração


# Retornando Valores #

#Para retornar valores, é usada a palavra reservada "return".
#Toda função Python retorna None por padrão.
#Diferente de outras linguagens, em Python, uma função pode retornar mais de um valor.

# Return #

def total(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(f'A soma dos números é:',total([21,17,35]),'\n')
#a função "total" recebe parâmetros "numeros" e retorna a soma desses "numeros" 
print(antecessor_sucessor(10))
#nesse caso a função "antecessor_sucessor" também recebe parâmetros "numeros", mas retorna dois valores definidos em operações
#dentro do escopo da própria função antecessor_sucessor.
#o valor retornado foi em formato de tupla, pois faz sentido serem imutáveis.

exibir_msg() #Bem vindo ao aprendizado de funções!!
print(exibir_msg()) #Bem vindo ao aprendizado de funções!!

                    #None
# "exibir_msg()" é diferente de "print(exibir_msg())", o segundo caso retorna um valor "None"


# Argumentos Nomeados #

#Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor

def salvar_jogo(nome, plataforma, ano, estilo):
    print(f'Jogo inserido com sucesso: {nome}/{plataforma}/{ano}/{estilo}')
#novamente insere argumentos dentro da função, cada argumento com seu nome próprio
salvar_jogo('Chrono Trigger', 'Snes', 1995, 'RPG')    
#a chamada é feita passando os dados de forma sequencial, caso erre a sequência, será atribuído valor errado
salvar_jogo(nome='Earthbound', ano=1994, plataforma='Snes', estilo='RPG')
#outra forma de fazer a chamada, mas que retorna os dados do mesmo jeito, mesmo mudando a ordem de ano e plataforma
salvar_jogo(**{'nome':'Sonic', 'plataforma':'MD', 'ano':1991, 'estilo':'adventure'})
#mais uma forma de fazer a chamada com os mesmos retornos
#os dois asteriscos são kwargs e informam que está passando um dicionário pra função


# Args e Kwargs #

#quando são definidos *args se refere a tuplas e **kwargs a dicionários .
#sendo assim é possível combinar parâmetros obrigatórios com args e kwargs.
#esses nomes são apenas convenções e podem ser valores, números, etc.

def exibir_poema(data_extenso,*args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}:{valor}'for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

    print(exibir_poema('Zen of Python', 'Beautiful is better than ugly.', autor='Tim Peters', ano=1999))




















