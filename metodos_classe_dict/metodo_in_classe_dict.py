# Método in -> O método de verificação in é uma forma mais elegante de verificar se uma chave existe ou não em nosso dicionário, 

contatos = {
    "ivaraleijado@gmail.com": {"nome": "Ivar", "telefone": "+47 936 25 147"},
    "sigurdolhodecobra@gmail.com": {"nome": "Sigurd", "telefone": "+47 986 36 784"},
    "Hvitserk@gmail.com": {"nome": "Hvitserk", "telefone": "+47 965 22 357"},
    "Ubbe@gmail.com": {"nome": "Ubbe", "telefone": "+47 974 85 963"}

}

resultaldo = "ivaraleijado@gmail.com" in contatos # True
print(resultaldo)

# Obs: Estou verificando se a chave "ivaraleijado@gmail.com" está no dicionário contatos. 

resultado = "idade" in contatos["ivaraleijado@gmail.com"] # False
print(resultado)

# Obs: Na segundo comando, estou solicitando que seja verificado se o atributo idade está contida na chave "ivaraleijado@gmail.com". 

resultado = "telefone" in contatos["ivaraleijado@gmail.com"] # True
print(resultado)

# Obs: No terceiro código estou verificando se o atributo telefone está contido na chave "ivaraleijado@gmail.com".

