import math
import numpy as np
import random

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
    pass
