# Funções -> Função é um bloco de código identificado por um nome (Identificador) e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada. 

# Exemplo

def exibir_mensagem(): # Função 1
    print("Olá mundo!")

def exibir_mensagem2(nome): # Função 2
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"): # Função 3
    print(f"Seja bem vindo {nome}!")

# exibir_mensagem()
# exibir_mensagem2(nome="Marcos")
exibir_mensagem3()
exibir_mensagem3(nome="Natália")

# obs: quando colocamos dois pontos estamos abrindo o bloco da minha função e tudo que estiver identado faz parte da minha função, voltando o recuo não faz mais parte. 
# A palavra resevada def determina ao python que se trata de uma função, exibir_mensagem é o nome dado a nossa função e (nome) seria nosso argumento. 

# Obs: Na função dois (linha 8 e 9), caso não seja passado um nome quando chamamos a função na linha 15 o código irá paresentar erro: (Traceback (most recent call last): 
#   File "c:\Users\marco\OneDrive\Área de Trabalho\Curso Dio\Exercícios Python\Funções\funcoes.py", line 15, in <module>
#     exibir_mensagem2()
# TypeError: exibir_mensagem2() missing 1 required positional argument: 'nome')

# Este erro significa que "Está função contém um argumento obrigatório que se chama (nome)" Você também pode passar o nome de forma direta Ex: exibir_mensagem2("Marcos").

# A função 3 tem uma diferençã da segunda, quando passamos um parâmetro na função como padrão caso não seja informado o valor no momento da chamada da função ele irá exibir o valor padrão determinado, que neste caso é "Anônimo", caso o nome seja informado será exibido assim como no exemplo abaixo. 
