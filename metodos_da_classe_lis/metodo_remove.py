# Remove: [].remove é uma segunda forma de se retirar um elemento de uma lista, diferente do pop ao invés de você passar o índice do seu objeto você passa o objeto em si. 

linguagens = ["Python", "js", "c", "java", "c"]

linguagens.remove("c")
print(linguagens)

# Obs: O remove funciona parecido com as demais opções na questão realizar a operação com base no primeiro índice identificado que foi especificado no código, sendo assim será removido apenas o primeiro objeto "c" que foi identificado. O que se pode fazer para remover tudo seria utilizar o count e identificar quantos objetos repetidos se tem e remover todos eles. 