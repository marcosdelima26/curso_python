# Por padrão uma lista em python funciona como uma pilha, quando adicionamos objetos na lista com o método append, ele irá para o fim da lista. 

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

# Obs: Quando utilizamos o pop do modo padrão ele irá retirar o último elemento adicionado, mas podemos passar também o índice que se deseja remover. 