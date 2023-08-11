# Utilizando quando desejos juntar listas, ou seja, temos duas listas diferentes e utilizando o extend onde as duas listas se tornaram uma, mesmo com valores duplicados elas serão unificadas, não excluindo valores duplicados na lista. 

linguagens = ["Python", "Java", "C#", "JavaScript", "Cobol", "Ruby"]

print(linguagens)

linguagens.extend(["c", "Delphi"])

print(linguagens)

