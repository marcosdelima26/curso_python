# método Setdefault -> Neste método se o atributo não estiver no dicionário, ele atribui o valor que foi adicionado, mas se o atributo existir no dicionário ele retorna o valor contido e não o informado. 

contatos = {"nome": "Marcos", "telefone": "(81) 3333-3333"}

print(contatos.setdefault("nome", "Natália")) # "Marcos"
print(contatos) # {"nome": "Marcos", "telefone": "(81) 3333-3333"}


print("=" * 70)
print("Neste exemplo o atributo (idade) não existe e assim ele será adicionado.")
print()
print(contatos.setdefault("idade", 28)) # 28
print(contatos) # {"nome": "Marcos", "telefone": "(81) 3333-3333", "idade": 28}