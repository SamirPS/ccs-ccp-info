# -*- coding: utf-8 -*-

import math
import numpy as np
import random

def test_generer_PI(f, n:int, cmax:int):
    print("[TEST] generer_PI(" + str(n) + ", " + str(cmax) + ")     : ", end="")
    result = f(n, cmax)
    try: assert(len(result) == n)
    except AssertionError: print("\nFailedTest : (Le résultat est de taille " + str(len(result)) + ", mais devrait être de taille " + str(n) + ")")
    else :
        try:
            outofbounds = [e for e in result if e[0] < 0 or e[0] > cmax or e[1] < 0 or e[1] > cmax]
            assert(len(outofbounds) == 0)
        except AssertionError: print("\nFailedTest : | Toutes les coordonées doivent se situer entre [0," + str(cmax) + "]." + "\n             | Premier élément ne respectant pas la règle : ["+ str(outofbounds[0][0]) +"," + str(outofbounds[0][1]) + "]")
        else : print("PASSED.")


def test_calculer_distances(f, PI:np.ndarray, n:int, cmax:int):
    print("[TEST] calculer_distances(PI) : ", end="")
    result = f(PI)
    try: assert(len(result) == n and len(result[0]) == n)
    except AssertionError: print("\nFailedTest : (Le résultat est de taille "+str(len(result[0]))+"x"+str(len(result))+", mais devrait être de taille "+str(n)+"x"+str(n)+")")
    else : print("PASSED.")

def generer_photo(n, m):
    return np.array([[int(random.randrange(0,255+1)) for j in range(m)] for i in range(n)])

testsetpi = np.array([[5,6], [6,4], [7,2], [5,2], [2,5], [0,6], [9,9], [6,0], [4,6], [7,6], [4,3], [7,0], [7,9], [3,10], [4,1]])


def position_robot(cmax=10):
    return random.randrange(0,cmax+1), random.randrange(0,cmax+1)

## NE RIEN CHANGER AU DESSUS DE CE COMMENTAIRE ---------------------------------




## I.A – Génération d’une exploration d’essai ----------------------------------
# I.A.1) Choix de points au hasard

def generer_PI(n:int, cmax:int) -> np.ndarray:
    pass

test_generer_PI(generer_PI, 17, 10) #Test automatique, si le test est PASSED vous pouvez passer à la suite.


# I.A.2) Calcul des distances

def calculer_distances(PI:np.ndarray) -> np.ndarray:
    pass


nombre_de_PI, cmax = 15, 10 #Vous pouvez changer les valeurs ici pour réaliser différents tests

#Test automatique, si le test est PASSED vous pouvez passer à la suite.
pi = generer_PI(nombre_de_PI, cmax)
test_calculer_distances(calculer_distances, pi, nombre_de_PI, cmax)






## I.B – Traitement d’image ----------------------------------------------------

# I.B.1) Analyse d’une image

def F1(photo:np.ndarray) -> np.ndarray:
    n = photo.min()
    b = photo.max()
    h = np.zeros(b - n + 1, np.int64)
    for p in photo.flat:
        h[p - n] += 1
    return h

# I.B.2) Sélection de points d’intérêts

def selectionner_PI(photo:np.ndarray, imin:int, imax:int) -> np.ndarray:
    pass






## II.A – Quelques fonctions utilitaires ---------------------------------------

# II.A.1) Longueur d’un chemin

def longueur_chemin(chemin:list, d:np.ndarray) -> float:
    pass

# II.A.2) Normalisation d’un chemin

def normaliser_chemin(chemin:list, n:int) -> list:
    pass






## II.C – Algorithme du plus proche voisin -------------------------------------

# II.C.1 - Plus proche voisin

def plus_proche_voisin(d:np.ndarray) -> list:
    pass





## III.A – Initialisation et évaluation ----------------------------------------

def creer_population(m:int, d:np.ndarray) -> list:
    pass







## III.B – Sélection -----------------------------------------------------------

def reduire(p:list) -> None:
    pass








## III.C – Mutation ------------------------------------------------------------

# III.C.1) muter_chemin

def muter_chemin(c:list) -> None:
    pass

# III.C.2) muter_population

def muter_population(p:list, proba:float, d:np.ndarray) -> None:
    pass








## III.D – Croisement ----------------------------------------------------------

# III.D.1) croiser

def croiser(c1:list, c2:list) -> list:
    pass

# III.D.2) nouvelle_génération

def nouvelle_generation(p:list, d:np.ndarray) -> None:
    pass


## III.E – Algorithme complet --------------------------------------------------

# III.E.1) algo_genetique

def algo_genetique(PI:np.ndarray, m:int, proba:float, g:int) -> float, list:
    pass
