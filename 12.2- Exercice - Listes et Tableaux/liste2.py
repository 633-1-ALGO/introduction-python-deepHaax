# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 444, 5, 7, 2], [2333, 24, 15, 75, 23]]

maxnb = 0

for i in range(0, len(tab)):

    for j in range(0, len(tab[i])):
        if tab[i][j] > maxnb:
            maxnb = tab[i][j]
            indiceN = i
            indiceM = j

print("La valeur maximum est :", maxnb, "et elle se trouve à l'indice [", indiceN, "][", indiceM, "]")
