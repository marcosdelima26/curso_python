# Método Fromkeys -> Este método ele cria chaves para você, podemmos usar em duas situações. 1º -> Desejo criar a chave e apenas colocar ela (chave) lá no dicionário, e não deseja adicionar nenhum valor. 

# 2º forma -> Você deseja criar um conjunto de chaves e deseja colocar um valor padrão nela, você cria as chaves com um valor vazio.

dict.fromkeys(["nome", "telefone"]) # Ex1: Retorno {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # Ex2: Retorno {"nome": "vazio", "telefone": "vazio"}

