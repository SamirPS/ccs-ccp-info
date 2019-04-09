# -*- coding: utf-8 -*-

# II.B.1) Écrire en Python une fonction nb_vol_par_niveau_relatif(regulation) qui prend en paramètre
# une régulation (liste de n entiers) et qui renvoie une liste de 3 entiers [a, b, c] dans laquelle a est le nombre de
# vols à leurs niveaux RFL, b le nombre de vols au-dessus de leurs niveaux RFL et c le nombre de vols au-dessous
# de leurs niveaux RFL.
def nb_vol_par_niveau_relatif(regulation):
  
  n=len(regulation)
  volsniveau=[0,0,0]
  
  for i in range(n):
    
    if regulation[i]==0:
      volsniveau[0]+=1
      
    elif  regulation[i]==1:
      volsniveau[1]+=1
      
    elif  regulation[i]==2:
      volsniveau[2]+=1
  return volsniveau
      
    
# II.B.2) Cout d’une régulation
# On appelle cout d’une régulation la somme des couts des conflits potentiels que cette régulation engendre.

## a) Écrire en Python une fonction cout_regulation(regulation) qui prend en paramètre une liste représentant
## une régulation et qui renvoie le cout de celle-ci.




## b) Évaluer en fonction de n, la complexité de cette fonction.




## c) Déduire de la question a) une fonction cout_RFL() qui renvoie le cout de la régulation pour laquelle chaque
## avion vole à son RFL.


# II.B.3) Combien existe-t-il de régulations possibles pour n vols ?
# Est-il envisageable de calculer les couts de toutes les régulations possibles pour trouver celle de cout minimal ?
