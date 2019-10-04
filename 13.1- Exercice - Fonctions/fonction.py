# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"

tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def afficherFrequenceLettreString(chaine,tabDeLettres):
    for i in range(0, len(tabDeLettres[0])):
        currentstring = tabDeLettres[0][i]
        for j in range(0, len(chaine)):
            if chaine[j] == currentstring:
                tabDeLettres[1][i] += 1
    print(tabDeLettres[1])


afficherFrequenceLettreString(texte, tab_lettres)

