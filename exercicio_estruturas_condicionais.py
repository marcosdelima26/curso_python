MAIOR_IDADE = 18
IDADE_ESPECIAL : 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH. ")

print("=" * 35)

# Estrutura com If/Else

idade_2 = int(input("Informe sua idade: "))

if idade_2 >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH. ")
else:
    print("Menor de idade, não pode tirar CNH.")

print("=" * 30)


# Estrutra com Elif

idade_3 = int(input("Informe sua idade: "))

if idade_3 >= MAIOR_IDADE:
    print("Informe sua idade: ")
elif idade_3 == IDADE_ESPECIAL:
    print("Pode falar aula teórica mas não a prática.")
else:
    print("Ainda não pode tirar a CNH.")