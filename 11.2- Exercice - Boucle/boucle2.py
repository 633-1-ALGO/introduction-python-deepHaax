# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié


A = [2, 6, 8, 5, 4, 12, 98, 34, 1]
print(A)

for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print (A)

