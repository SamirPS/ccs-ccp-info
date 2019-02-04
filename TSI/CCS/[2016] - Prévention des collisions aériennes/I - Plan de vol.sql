I.A – Écrire une requête SQL qui fournit le nombre de vols qui doivent décoller dans la journée du 2 mai 2016 avant midi.

SELECT COUNT(DISTINCT id_vol) FROM vol WHERE jour = '2016-05-02' AND heure <= '12:00';

I.B – Écrire une requête SQL qui fournit la liste des numéros de vols au départ d’un aéroport desservant Paris le 2 mai 2016.

SELECT id_vol
    FROM vol
        JOIN aeroport AS a ON a.ville = 'Paris'
    WHERE
        a.ville = 'Paris' AND
        jour = '2016-05-02';

I.C – Que fait la requête suivante ?
SELECT id_vol
    FROM vol
        JOIN aeroport AS d ON d.id_aero = depart
        JOIN aeroport AS a ON a.id_aero = arrivee
    WHERE
        d.pays = 'France' AND
        a.pays = 'France' AND
        jour = '2016-05-02'


I.D – Certains vols peuvent engendrer des conflits potentiels : c’est par exemple le cas lorsque deux avions suivent un même trajet, en sens inverse, le même jour et à un même niveau. Écrire une requête SQL qui fournit la liste des couples (Id 1 , Id 2 ) des identifiants des vols dans cette situation.
