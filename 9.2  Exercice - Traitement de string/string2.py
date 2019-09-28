# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.

# Ex1
print("Researche number of occurence 'exemple' in the string 'text'")
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
soustext = "exemple"
# count "exemple" in string "texte"
count = texte.count("exemple")
print("String = ", texte)
print("Nombre de mot 'exemple' dans le string : ", count)

print("-----------")

# Ex2
print("Replace word 'est' in the string 'texte' for 'représente'")
print (texte.replace("est", "représente"))

print("-----------")

# Ex3
print("inverse direction of reading of the string 'texte'")
print(texte[::-1])


