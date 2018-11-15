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

def position_robot(cmax=10):
    return random.randrange(0,cmax+1), random.randrange(0,cmax+1)

## NE RIEN CHANGER AU DESSUS DE CE COMMENTAIRE ---------------------------------




# I.A – Génération d’une exploration d’essai
## I.A.1) Choix de points au hasard

def generer_PI(n:int, cmax:int) -> np.ndarray:
    liste_points = []
    for k in range(n):
        x = random.randrange(0,cmax+1)
        y = random.randrange(0,cmax+1)
        liste_points.append([x,y])
    return np.array(liste_points)

test_generer_PI(generer_PI, 17, 10) #Test automatique, si le test est PASSED vous pouvez passer à la suite.


## I.A.2) Calcul des distances

def calculer_distances(PI:np.ndarray) -> np.ndarray:
    distances, buffer = [],[]
    x_r, y_r = position_robot()
    for i in range(0, PI.shape[0]):
        x1, y1 = PI[i][0],PI[i][1]
        for j in range(0, PI.shape[0]):
            x2, y2 = PI[j][0],PI[j][1]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            buffer.append(distance)
        distances.append(buffer)
        buffer = []
    return np.array(distances)


nombre_de_PI, cmax = 15, 10 #Vous pouvez changer les valeurs ici pour réaliser différents tests

#Test automatique, si le test est PASSED vous pouvez passer à la suite.
pi = generer_PI(nombre_de_PI, cmax)
test_calculer_distances(calculer_distances, pi, nombre_de_PI, cmax)
