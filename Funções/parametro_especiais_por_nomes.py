# Keyword only -> Parâmetros especiais por nome, será necessário passar cada parâmetro. 

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, combustivel)

criar_carro(modelo="Compass", ano=2023, placa="DEF-5678", marca="Jeep", motor="2.0", combustivel="Flex") # Válido

# criar_carro("Compass", 2023, "DEF-5678,", marca="Jeep", motor="2.0", combustivel="Flex") # Opção inválida. 


