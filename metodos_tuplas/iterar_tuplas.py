# Iterar tuplas -> A forma mais comum para percorrer os dados de uma tupla é utilizando o comando for. 

# For
carros = ("gol", "celta", "palio", )

for carro in carros:
    print(carro)

print("=" * 50)

# Função Enumerate -> Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

carros = ("gol", "celta", "palio", )

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

