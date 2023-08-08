# Interpolação: Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última utlizando f strings. A primeita forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo vamos focar nas duas últimas. 

nome = "Marcos"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Nome: %s Idade: %d" % (nome, idade)) # Forma não mais utilizada

print("Nome: {1} Idade: {0}".format(idade, nome)) # Forma não mais utilizada

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.") # Forma utilizada do Python 3 em diante

print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem)) # Forma utilizada do Python 2 em diante

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho coo {profissao} e estou matriculado no curso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Exibindo casas decimais após o ponto em caso de um float

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")     # Quando adiciona .2 significa que são duas casas decimais.
print(f"Valor de PI: {PI:10.2f}")   # Desta forma adicionamos espaço antes da casa decimal.