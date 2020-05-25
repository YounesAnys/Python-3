#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice4 lab4
#Factorielle

def calculeFact(n):
    reponse = 1
    i = 1
    while i <= n :
       reponse = reponse * i
       i = i + 1
    return reponse
print("Calcul de la factorielle de n")
n = int(input("Entrez un nombre positif"))
if n < 0:
   print("Le nombre ne doit pas etre negatif, veuillez ecrire un nouveau nombre")
elif n >= 0:
    print(n)
    print("La factorille vaut",calculeFact(n))
    
