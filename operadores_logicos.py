# Operadores lógicos "São operadores utilizados em conjunto com os operadores de comparação, para montar um expressão lógica. Quando um operador de compração é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo: "

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)

print(saldo <= limite)

print("=" * 20)

# Tipos de Operadores Lógicos
# And (E) verifica se uma condição e outra são verdadeiras.
# Or (ou) Verifica se uma ou outra condição é verdadeira.
# Not (Não) Inverte uma condição, se ela é verdadeira se torna falsa.

# Operador And
print(saldo >= saque and saque <= limite) # Resultado (False) Pois para ser verdadeiro as duas condições precisam ser verdadeiras. 

# Operador Or
print(saldo >= saque or saque <= limite) # Resultado (True) Pois uma das duas condições são verdadeiras.

# Operador Not 
print(not 1000 > 1500) # Resultado (True) Pois a condição é falsa sendo assim inverte o resultado da condição.

