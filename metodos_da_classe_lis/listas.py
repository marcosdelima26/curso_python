# Listas: Lista em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes. Lista são objetos mutáveis, portanto podemos alterar seus valores após a criação. 

frutas = ["Laranja", "Maça", "Uva"] # Lista com strings

frutas_2 = [] # Lista vazia

letras = list("Python") # Fará um lista onde cada letra é um elemento. P-y-t-h-o-n

numeros = list(range(10)) # Fará uma lista utilizando a função range ela vai gerar valores de 0-9

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] # Dados do Carro, como marca, Modelo, KM rodados, Ano, IPVA, Cidade de registro do carro 

print(frutas)
print(frutas_2)
print(letras)
print(numeros)
print(carro)

# Acesso Direto: Temos mais de uma forma de realizar o acesso a uma lista, um deles é o acesso direto: A lista é uma sequência, portanto podemos acessar seus dados utilizando o índice de determinada sequência a partir do zero. 

print(letras[3])

# Índices negativos: Podemos acessar a posição com números negativos

print(frutas[-1]) # O -1 indica o último elemento da lista. De acordo com que vamos aumentando os número -2, -3 ele vai acessando os demais itens. 

# Lista aninhadas: Listas podem armazenar todos os tipos de objetos PPython, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturass bidimensionais (Tabelas), e acessar informando os índices de linha e coluna. 

print("=" * 60)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]

]

print(matriz[0])    # Consultando a primeira linha, Resultado [1, "a", 2]
print(matriz[0][0]) # Consultando o elemento 1, linha 0 indíce 0
print(matriz[0][1]) # Consultando o elemento 2, linha 0 índice -1
print(matriz[-1][-1]) # Consultando o elemento "c", linha -1 e índice -1

# Se deseja pegar um linha basta abrir colchetes uma única vez e digitar o número da linha, caso queira um elemento específico, abrir colchetes duas vezes e primeiro você informa a linha e depois o índice do elemento. 



