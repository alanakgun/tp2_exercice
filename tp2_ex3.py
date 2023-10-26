#Exerice 3 : echange de trois valeurs
a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

temp = b
b = a
a = c
c = temp

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)