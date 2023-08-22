# Método del -> Este método você precisa passar para ele o valor que deseja remover.

contatos = {
    "ivaraleijado@gmail.com": {"nome": "Ivar", "telefone": "+47 936 25 147"},
    "sigurdolhodecobra@gmail.com": {"nome": "Sigurd", "telefone": "+47 986 36 784"},
    "Hvitserk@gmail.com": {"nome": "Hvitserk", "telefone": "+47 965 22 357"},
    "Ubbe@gmail.com": {"nome": "Ubbe", "telefone": "+47 974 85 963"}

}

del contatos["ivaraleijado@gmail.com"]["telefone"]
del contatos["sigurdolhodecobra@gmail.com"]

print(contatos)

# obs: Na linha 11 o del irá apenas remover o número de telefone da chave "ivaraleijado@gmail.com", pois se for passado a chave e em seguida um atributo ele vai remover o atributo especificado da chave informada. 
# obs 2: Já na linha 12 será realizado a remoção da chave "sigurdolhodecobra@gmail.com" pois foi especificado apenas a chave e assim todos os seus atributos e valores serão removidos. 

# obs 3: Caso você deseja apagar todo o dicionário basta colocar o comando del contatos.