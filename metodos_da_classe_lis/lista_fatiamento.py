# Fatiamento: Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursos deve "Pular" no acesso. 

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])    # ["t", "h", "o", "n"]
print(lista[0:2])   # ["p", "y"]
print(lista[1:3])   # ["y", "t"]
print(lista[0:3:2]) # ["p", "t"]
print(lista[::])    # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

print("=" * 50)

# Iterar Listas: A forma mais comum para percorrer os dados de uma lista é utilizando o comando for. 

carros = ["Compass", "Corolla", "A4"]

for carro in carros:
    print(carro)


print("=" * 50)

# Função Enumerate: Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate. 

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


print("=" * 50)

 # Compreensão de listas (List comprehasion): A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros: 
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

print("=" * 50)


# Comprehasion

numeros_2 = [1, 30, 21, 2, 9, 65, 34]
pares_2 = [numero for numero in numeros_2 if numero % 2 == 0]

print("=" * 50)

# Modificando valores versão 1.0

numeros_3 = [1, 30, 21, 9, 65, 34]
quadrado = []

for numero in numeros_3:
    quadrado.append(numero ** 2)


# ou com Comprehasion

numeros_4 = [1, 30, 21, 2, 9, 65, 34]
quadrado_2 = [numero ** 2 for numero in numeros_4]

