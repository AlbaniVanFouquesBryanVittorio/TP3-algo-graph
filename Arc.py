import Noeud

class Arc :
     def __init__(self, som1 : Noeud, som2 : Noeud, valeur : int, marque : int ): 
         self.som1 = som1 # une des extrémités de l'arêteZ
         self.som2 = som2 # l'autre extrémité de l'arête
         self.valeur = valeur # Pour les arêtes étiquetées
         self.marque = marque # une marque, utile pour certains algorithmes


ListeAdjacence  = {
        
        1 : [2,5],
        2 : [3,5],
        3 : [4,7],
        4 : [3,8],
        5 : [1,6],
        6 : [7],
        7 : [],  
        8 : [4,7],
        
        }


