# Método copy -> Fará uma cópia do nosso dicionário. 

contatos = {
        "marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-2536"},
        "afrodite@gmail.com": {"nome": "Afrodite", "telefone": "(11) 99486-3225"},
        "Zeus@hotmail.com": {"nome": "Zeus", "telefone": "(85) 98524-3789"},
        "thorfilhodeodin@gmail.com": {"nome": "Thor", "telefone": "(13) 99999-9998"}
}

copia = contatos.copy()
copia["afrodite@gmail.com"] = {"nome": "Deusa"}

print(contatos["afrodite@gmail.com"])

print(copia["afrodite@gmail.com"])