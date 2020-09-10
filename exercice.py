#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    distance_minuscule_majuscule = 32
    for lettre in mot:
        # TODO completer la fonction ici
        if ord(lettre) >= 97 & ord(lettre) <= 122
            lettre = ord(lettre) - distance_minuscule_majuscule
        resultat += chr(lettre)
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
