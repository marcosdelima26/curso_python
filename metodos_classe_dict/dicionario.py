# Dicionário -> Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {} ou dict, e contém uma lista de pares chave:valor separada por vírgulas. 

pessoa = {"nome": "Guilherme", "idade": 28} # Chave: nome, idade

pessoa = dict(nome="Marcos", idade=28)

pessoa["telefone"] = "3361-2857"

# Consultando um dicionário -> para consultar o dicionário basta informar o nome do dicionário e a chave que deseja consultar.  Exemplo!

dados = {"nome": "Marcos", "idade": 28, "telefone": "3368-2751"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])
print("=" * 20)
# Alterando os valores do dicionário -> Basta especificar o dicionário e a chave e informar o valor que deseja substituir pelo valor que está la dentro. 

dados["nome"] = "Natália"
dados["idade"] = 24
dados["telefone"] = "(81) 98587-7177"

print(dados)


