# A classe string do python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar. Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

curso = "pYtHon"
curso_2 = "        Python  "
curso_3 = "Python"

print(curso.upper())    # Converte todos os caracteres para Maiúsculo
print(curso.lower())    # Converte todos os caracteres para Minúsculo
print(curso.title())    # Converte todos os caracteres exceto a primeira letra para Minúsculo.

print("=" * 20)

print(curso_2.strip())    # Remove todos os espaços
print(curso_2.lstrip())   # Remove todos os espaços do lado esquerdo da palavra
print(curso_2.rstrip())   # Remove todos os espaços do lado direito da palavra

print("=" * 20)

print(curso_3.center(10, "#"))  # Centraliza a palavra, o método center ele tem dois argumentos, onde o primeiro irá especificar a quantidade de caracteres e o segundo será o caracter que irá substituir os espaços em branco para completar o primeiro argumento. Caso não seja adicionado nada ele vai preencher com espaços em branco. 

print("." .join(curso_3))   # o método join ele funciona com todo tipo de iterável, ele vai passar item a item e vai adicionar o caractere informado a cada letra que ele passar. 



