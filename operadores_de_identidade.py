# Operadores de identidade: São utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória. 

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)


print("=" * 20)

# Operador de identidade (is) faz uma verificação se ambos os valores ocupam a mesma região de memória. 

saldo = 10000
limite = 5000

print(saldo is limite)
print(saldo is not limite)
