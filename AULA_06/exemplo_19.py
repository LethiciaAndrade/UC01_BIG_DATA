# Listas
nomes_01 = "Alessandro, Maria, Pedro, Duda, Eduardo"
nomes_02 = ["Alessandro", "Maria", "Pedro", "Duda", "Eduardo", "Manoel"]
print(nomes_01)
print(nomes_02)
print(nomes_02 [2])
print(len(nomes_02)) # len- serve para mostrar o comprimento do vetor, quantos registros têm no vetor.
n = 1
for i in range (len(nomes_02)): # for i in... - serve para colocar um embaixo do outro (range- serve para colocar o nº de repetições que você quer)
    print(f"{n} - {nomes_02 [i]}")
    n += 1

