while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

print(numero)

print("=" * 70)

# Utilizando Break com For (Break: utilizado quando desejamos forçar uma parada.)

for numero in range(100):

    if numero == 10:
        break

    print(numero, end=" ")

print()
print("=" * 70)
# Utilizando o coninue: Utilizado quando queremos desviar de uma situação e continuar executando o código.

for numero in range(100):
    if numero == 20:
        continue

    print(numero, end=" ")

