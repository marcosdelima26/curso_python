# Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina. 

# Utilziando espaços no Python
# Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco. 

def sacar(self, valor: float) -> None: # início do bloco do método

    if self.saldo >= valor: # Início do bloco do if

        self.saldo -= valor

    # fim do bloco do if

# fim do bloco do método

# Se não houver a identação o python não irá rodar o código. 
