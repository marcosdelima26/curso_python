# Método copy ele irá retornar uma lista igual, entretanto, não será a mesma lista. 
lista = [1, "python", [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista)) # Verificando o id vamos confirmar que as listas apesar de conter a mesma informação são listas diferentes.

print("=" * 30)

# Adicionando uma informação na l2

l2[0] = 2

print(l2)
print(lista)



