#Exercice 1 : variables/affectation :

x = int(input("Entrez x : "))
y = int(input("Entrez y : "))

print("Avant permutation")
print("x :", x)
print("y :", y)

temp = x
x = y
y = temp

print("Après permutation")
print("x :", x)
print("y :", y)
