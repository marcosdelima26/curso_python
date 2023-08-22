# Método Update -> Este método permite atualizar o dicionário atual, onde passamos um novo dicionário e os novos valores são adicionados. Se você realizar o update de uma chave já existente e passar o atributo nome como especificado, ao invés dele adicionar, ele vai substituir. Agora se você passa um novo dicionário e essas chaves não existem, ele vai atualizar e adiconar a nova chave e valores informados. 

contatos = {
    "Björnironside@gmail.com": {"nome": "Björn", "telefone": "+47 947 87 952"}
}

contatos.update({"Björnironside@gmail.com": {"nome": "Grande Rei"}})
print(contatos) # {"Björnironside@gmail.com": {"nome": "Grande Rei"}

contatos.update({"striker@gmail.com": {"nome": "Striker", "telefone": "4444-5555"}})
print(contatos) # {'Björnironside@gmail.com': {'nome': 'Grande Rei'}, 'striker@gmail.com': {'nome': 'Striker', 'telefone': '4444-5555'}}
