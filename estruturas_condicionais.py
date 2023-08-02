# Estruturas condicionais: A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas. 

# IF: Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas. 

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
if saldo < saque:
    print("Saldo insuficiente!")

# If/else: Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de cógigo do if será executado. Caso contrário o bloco de código do else será executado. 

saldo_2 = 2000.0
saque = float(input("Informa o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# If/elif/else: Em alguns cenários queremos mais de dois devios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código. 

opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quatia para saque: "))
elif opcao == 2:
    print("Exibindo o Extrato... ")
else:
    sys.exit("Opção inválida, Tente novamente!")

