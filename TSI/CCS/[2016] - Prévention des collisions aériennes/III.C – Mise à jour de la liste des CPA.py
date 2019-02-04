# -*- coding: utf-8 -*-


# III.C.1) Écrire en Python une fonction mettre_a_jour_CPAs(CPAs, id, nv_CPA, intrus_max, suivi_max)
# qui prend en paramètre
# − CPAs : la liste actuelle des CPA au format décrit ci-dessus ;
# − id : l’identifiant d’un intrus ;
# − nv_CPA : les caractéristiques du CPA de l’intrus telles que renvoyées par la fonction calcul_CPA (peut
# éventuellement valoir None) ;
# − intrus_max : un entier indiquant le nombre maximum d’intrus à suivre ;
# − suivi_max : un entier donnant le délai maximum (en secondes) avant un CPA pour s’intéresser à l’intrus
# correspondant.
# Cette fonction modifie la liste CPAs en appliquant les règles suivantes :
# − si l’avion id est déjà suivi et ne présente plus de risque de collision, ou si son CPA est prévu dans plus de
# suivi_max secondes, il est supprimé de la liste ;
# − si l’avion id est déjà suivi et que son CPA est prévu dans moins de suivi_max secondes, la ligne correspon-
# dante est mise à jour avec les nouvelles informations sur le CPA ;
# − si l’avion id n’est pas suivi et que son CPA est prévu dans moins de suivi_max secondes alors,
# • s’il reste de la place dans la liste il est ajouté à la fin,
# • si la liste est pleine (elle contient déjà intrus_max intrus) et si le tCPA du nouvel intrus est inférieur au
# tCPA du dernier de la liste alors le nouvel intrus remplace le dernier intrus de la liste.
# 2016-03-13 14:33:27
# Page 6/7La fonction mettre_a_jour_CPAs renvoie :
# − None si l’avion id a été supprimé ou n’a pas été ajouté ;
# − ou un entier indiquant l’indice de la ligne de CPAs qui a été modifiée ou ajoutée.


def mettre_a_jour_CPAs(CPAs:list, id, nv_CPA, intrus_max:int, suivi_max:int):
    pass


# III.C.2) Suite à un appel à la fonction mettre_a_jour_CPAs, il se peut que la liste CPAs ne soit plus triée par
# ordre croissant des tCPA.
# Écrire en Python une fonction replacer(ligne, CPAs) qui modifie la liste CPAs de façon à ce qu’elle soit
# ordonnée par tCPA croissant, en sachant que la seule ligne qui n’est éventuellement pas à sa place est celle
# d’indice ligne.
# Autrement dit, la fonction replacer(ligne, CPAs) doit remettre la ligne CPAs[ligne] à sa place dans l’ordre
# des tCPA croissants.




# III.C.3) Écrire en Python la fonction enregistrer_CPA utilisée par la fonction TCAS (figure 5).
