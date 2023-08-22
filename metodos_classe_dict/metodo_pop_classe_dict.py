# Método pop -> Ele remove um valor do seu diconário (Chave) e caso ela não exista você pode informar um valor padrão para ela retornar. Além disso quando ele encontra a chave informada ele irá retornar o valor que ele removeu do dicionário. 

contatos = {
        "marcosads2021@gmail.com": {"nome": "Marcos", "telefone": "(81) 99996-2536"},
        "afrodite@gmail.com": {"nome": "Afrodite", "telefone": "(11) 99486-3225"},
        "Zeus@hotmail.com": {"nome": "Zeus", "telefone": "(85) 98524-3789"},
        "thorfilhodeodin@gmail.com": {"nome": "Thor", "telefone": "(13) 99999-9998"}
}

print(contatos.pop("afrodite@gmail.com")) # {"nome": "Afrodite", "telefone": "(11) 99486-3225"}

print(contatos.pop("torinfilhodetrain@gmail.com", {})) # {}

print("=" * 115)
print("Dicionário após remoção de uma das chaves")
print()
print(contatos)