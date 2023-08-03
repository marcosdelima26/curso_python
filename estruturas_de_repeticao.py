# Estrutras de repitação são duas For e While.
# O que são estruturas de repetição: São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica. 

# Comando For: O comando for é usado para percorrer um objeto iterável. Faz sentido usar quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável. 

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# For/Else

texto = input("Informe um texto: ")
VOGAIS_2 = "AEIOU"

for letra in texto:
    print(letra, end="")
else:
    print()
    print("Executa no final do laço")

