# -*- coding: utf-8 -*-

import math
import numpy as np
import random

def generer_photo(n, m):
    return np.array([[int(random.randrange(0,255+1)) for j in range(m)] for i in range(n)])

testsetpi = np.array([[5,6], [6,4], [7,2], [5,2], [2,5], [0,6], [9,9], [6,0], [4,6], [7,6], [4,3], [7,0], [7,9], [3,10], [4,1]])

## NE RIEN CHANGER AU DESSUS DE CE COMMENTAIRE ---------------------------------





# I.B – Traitement d’image

## I.B.1) Analyse d’une image

def F1(photo:np.ndarray) -> np.ndarray:
    n = photo.min()
    b = photo.max()
    h = np.zeros(b - n + 1, np.int64)
    for p in photo.flat:
        h[p - n] += 1
    return h

## I.B.2) Sélection de points d’intérêts

def selectionner_PI(photo:np.ndarray, imin:int, imax:int) -> np.ndarray:
    PI_selectionnes = []
    for x in range(photo.shape[0]):
        for y in range(photo.shape[1]):
            i = photo[x][y]
            if i >= imin and i <= imax:
                PI_selectionnes.append([x, y])
    return np.array(PI_selectionnes)

photo = generer_photo(5,5)
print(photo)
print(selectionner_PI(photo, 100, 200))

