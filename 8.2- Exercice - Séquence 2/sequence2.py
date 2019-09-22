# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75

taxe = 0.077
prixarajouter = prix_ht*taxe

prix_ttc = prix_ht+prixarajouter

print("Le prix TTC est de", prix_ttc*nb_articles, " chf")
