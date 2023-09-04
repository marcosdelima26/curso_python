# Keyword and Positional only -> Parâmetro por posição e nome. 

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Maserati Ghibli", 2021, "GHI-9012", marca="Maserati", motor="2.0", combustivel="Flex") # Válido

# criar_carro(modelo="Maserati Ghibli", ano=2021, placa="GHI-9012", marca="Maserati", motor="2.0", combustivel="Flex") # Inválido

