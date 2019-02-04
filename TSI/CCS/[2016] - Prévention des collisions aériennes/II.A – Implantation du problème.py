# -*- coding: utf-8 -*-

conflit = [
    [   0,   0,   0, 100, 100,   0,   0, 150,   0],
    [   0,   0,   0,   0,   0,  50,   0,   0,   0],
    [   0,   0,   0,   0, 200,   0,   0, 300,  50],
    [ 100,   0,   0,   0,   0,   0, 400,   0,   0],
    [ 100,   0, 200,   0,   0,   0, 200,   0, 100],
    [   0,  50,   0,   0,   0,   0,   0,   0,   0],
    [   0,   0,   0, 400, 200,   0,   0,   0,   0],
    [ 150,   0, 300,   0,   0,   0,   0,   0,   0],
    [   0,   0,  50,   0, 100,   0,   0,   0,   0]
]


# II.A.1) Écrire en Python une fonction nb_conflits() sans paramètre qui renvoie le nombre de conflits po-
# tentiels, c’est-à-dire le nombre d’arêtes de valuation non nulle du graphe.


def nb_conflits(): # O(n²)
    global conflit
    count = 0
    for line in conflit:
        #print(line) #Décommentez cette ligne pour suivre la progression de l'algorithme
        for element in line:
            if element != 0:
                count += 1
    return count / 2

## Une autre possibilité plus optimisée !

def nb_conflits_opti(): # O(n² / 2)
    global conflit
    count = 0
    for yk in range(len(conflit)):
        #print(conflit[yk][:yk+1]) #Décommentez cette ligne pour suivre la progression de l'algorithme
        for element in conflit[yk][:yk+1]:
            if element != 0:
                count += 1
    return count


# II.A.2) Exprimer en fonction de n la complexité de cette fonction.

# nb_conflits()       =>  O(n²)
# nb_conflits_opti()  =>  O(n² / 2)