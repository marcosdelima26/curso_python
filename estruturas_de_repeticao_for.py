texto = ""
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

# Exemplo utilizando função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")