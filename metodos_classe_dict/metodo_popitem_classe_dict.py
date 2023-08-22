# Metodo popitem -> Este método ele vai remover as chaves em sua sequência original, sem precisar informar qual chave desse ser removida e caso não exista mais chave ele retorna KeyError. 

contatos = {
        "marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-2536"},
        "afrodite@gmail.com": {"nome": "Afrodite", "telefone": "(11) 99486-3225"},
        "Zeus@hotmail.com": {"nome": "Zeus", "telefone": "(85) 98524-3789"},
        "thorfilhodeodin@gmail.com": {"nome": "Thor", "telefone": "(13) 99999-9998"}
}

print(contatos.popitem()) #  "thorfilhodeodin@gmail.com": {"nome": "Thor", "telefone": "(13) 99999-9998"}

print(contatos.popitem()) # "Zeus@hotmail.com": {"nome": "Zeus", "telefone": "(85) 98524-3789"},

print(contatos.popitem()) # "afrodite@gmail.com": {"nome": "Afrodite", "telefone": "(11) 99486-3225"},

print(contatos.popitem()) # "marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-2536"},

print(contatos.popitem()) # KeyError