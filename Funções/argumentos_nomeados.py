# Argumento nomeados -> Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor. 

def salvar_carro(marca, modelo, ano, placa): 
    # Salvar carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Carro inserido com sucesso" Fiat/Palio/1999/ABC-1234

# Na linha 3 estamos passando marca, modelo, ano e placa como argumentos. 

# Na linha 7 estamos realizando a chamada da função através de uma forma sequencial, informando as características do carro. Entretanto esta forma de chamada se tem uma desvantagem, pois se os valores informados forem invertidos o python não irá identificar que estão errados, e as informações serão adicionadas mesmo assim. Ex: salvar_carro("Palio", "Fiat", 1999, "ABC-1234")

# Na linha 8 estamos realizando a chamada da função passando o conjunto chave=valor e precisamos respeitar os argumentos passados na função. Além de uma vantagem comparada a primeira chamada, onde você já específica o a chave mais o valor evitando que valores sejam adiconados de forma trocadas, mas também existe uma desvantagem se em algum momento o desenvolvedor altera o argumento e esquece de comunicar a equipe, será gerado um erro no código. 

# Na linha 9 está sendo passado um dicionário para a função (salvar_carro). Os dois asterísticos informa que você está passando um dicionário pra a função e vai gerar algo parecido com (marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") 