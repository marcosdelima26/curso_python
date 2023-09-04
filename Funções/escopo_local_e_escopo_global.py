# Escopo Local e Escopo Global -> Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global. 
#OBS: Essa não pe uma boa prática e deve ser evitada. 

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

novo_salario = salario_bonus(500) # 2500
print(novo_salario)