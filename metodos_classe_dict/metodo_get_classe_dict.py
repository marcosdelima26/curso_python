# Método get -> O método get é uma segunda forma de se acessar valores em um dicionário. 

contatos = {
        "marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-2536"},
        "afrodite@gmail.com": {"nome": "Afrodite", "telefone": "(11) 99486-3225"},
        "Zeus@hotmail.com": {"nome": "Zeus", "telefone": "(85) 98524-3789"},
        "thorfilhodeodin@gmail.com": {"nome": "Thor", "telefone": "(13) 99999-9998"}
}

# print(contatos["chave"]) # KeyError -> Este erro foi adicionado ao código propositalmente 

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # {} Default
print(contatos.get("marcosads2021@gmail.com", {})) # {"marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-3225 "}}

# Obs: Se você coloca um chave que não está no dicionário, o get fará uma excessão. Utilizado quando não se sabe se a chave existe no dicionário, quando não encontra a chave ele retorna none, ou retorno de valor default (dicionário vazio).