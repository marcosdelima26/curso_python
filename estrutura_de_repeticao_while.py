# Comando While: O comando While é usado para repetir um bloco de código várias vezes. Faz sentido usar While quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado. 

# Exemplo
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o Extrato... ")

# While\Else

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        (print("Sacando... "))
    elif opcao == 2:
        print("Exibindo o Extrato... ")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

