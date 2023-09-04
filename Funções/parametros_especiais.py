# Parâmetros especiais -> Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual o argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome. 

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Range Rover Evoque", 2023, "ABC-1234", marca="Range Rover", motor="2.0", combustivel="Flex")   # Válido

# criar_carro(modelo="Range Rover Evoque", ano=2023, Placa="ABC-1234", marca="Range Rover", motor="2.0", combustivel="Flex")  # Inválido

# A segunda opção não é válida pois a / obriga a ser só por posição. 
# Parâmetros após a barra pode ser pasado por parâmetro ou posição, antes da barra é obrigatório por posição. 


