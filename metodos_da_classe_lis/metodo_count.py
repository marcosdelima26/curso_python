# Count: [].count ele é utilizado para contar quantas vezes um objeto aparece em sua lista. 

cores = ["Vermelho", "Azul", "Verde", "Azul"]

print(cores.count("Vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#OBS: todas as cores estão existentes na lista, entretanto o erro ocorre devido a o código solicitar buscar a informação com letra minúscula e ela se encontra com a primeira letra maiúscula. Isso ocorre pois o python é case sensitive. 