#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice3 lab4

import random
n = random.randint(1,10)
def devine(x):
    a = 0
    tentative = 1
    while a != n:
        a = int(input("Veuillez entrer un nombre"))
        if a != n:
            tentative = tentative + 1
        if a < n:
            print("L'essai est bas, veuillez entrer un nouveau nombre")
        if a > n:
            print("L'essai est haut, veuillez entrer un nouveau nombre")
    return tentative
print("Félicitation vous avez deviné le bon nombre votre nobre de tentatives est:", devine(n))
