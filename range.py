# Função Range: Range é uma função buil-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido:

#       i, i+1, i+2, i+3 ...., j-1

#Ele recebe argumentos: stop(Obrigatório), start (Opcional) e step opcional.

print(list(range(4)))

# Range com for

for numero in range (0, 11):
    print(numero, end= " ")

print()

# Exibindo tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end= " ")
