# Retornando valores na função -> Para retornar um valor, utilizamos a palavra reservada (return). Toda função python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor. 

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34])) # 64
print(retorna_antecessor_e_sucessor(10)) # (9, 11)
print("=" * 20)

# obs: Se eu tenho um função e ela não tem um valor explícito, o retorno por padrão será none. Exemplo:

def func_3():
    print("Olá mundo!")

print(func_3())