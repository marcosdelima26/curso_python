# Tuplas aninhadas -> Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna. 

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),

)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][1])
print(matriz[-1][-1])
