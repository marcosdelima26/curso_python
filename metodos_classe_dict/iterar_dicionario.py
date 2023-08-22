contatos = {
    "111.222.333.44": {"nome": "Marcos", "idade": 28, "telfone": "(81) 98854-3362"},
    "222.333.444.55": {"nome": "Rafael", "idade": 35, "telefone": "(81) 93365-5896"}

}

print("Primeira forma de utilizar o FOR")
print()
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

print("Segunda forma de utilizar o FOR")
print()

for chave, valor in contatos.items():
    print(chave, valor)

# Método items -> retorna uma lista de tuplas, nesta lista de tuplas o primeiro argumento é a chave o segundo é o valor. 