# Dicionários Aninhados -> Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números).

contatos = {
        "marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-2536"},
        "afrodite@gmail.com": {"nome": "Afrodite", "telefone": "(11) 99486-3225"},
        "Zeus@hotmail.com": {"nome": "Zeus", "telefone": "(85) 98524-3789"},
        "thorfilhodeodin@gmail.com": {"nome": "Thor", "telefone": "(13) 99999-9998", "extra": {"a": 25}}
       }


telefone = contatos["afrodite@gmail.com"]["telefone"]
print(telefone)

extra = contatos["thorfilhodeodin@gmail.com"]["extra"]["a"]
print(extra)

