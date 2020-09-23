import Arc

class Sommet :
    def __init__(self, num : int, marque : int, arc : [Arc]):     
        self.num = num # Un entier pour identifier un sommet
        self.marque =  marque # une marque, utile pour certains algorithmes
        self.adjacents = arc # une liste des arêtes adjacentes

