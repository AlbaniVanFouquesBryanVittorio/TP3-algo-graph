import Graph 
import Sommet

#exemple de création de Graph

ListSommet = []
s1 = Sommet.Sommet(1, 0, None)
ListSommet.append(s1)

s2 = Sommet.Sommet(2,0, None)
ListSommet.append(s2)


s3 = Sommet.Sommet(3, 0, None)
ListSommet.append(s3)

s4 = Sommet.Sommet(4, 0, None)
ListSommet.append(s4)

s5 = Sommet.Sommet(5, 0, None)
ListSommet.append(s5)

s6 = Sommet.Sommet(6, 0, None)
ListSommet.append(s6)

s7 = Sommet.Sommet(7, 0, None)
ListSommet.append(s7) 

s8 = Sommet.Sommet(8, 0, None)
ListSommet.append(s8) 

G = Graph.Graph(ListSommet)
G.ajouterArcValue(s1, s2, 16);
G.ajouterArcValue(s1, s3, 12);

G.ajouterArcValue(s2, s4, 8);
G.ajouterArcValue(s2, s5, 8);

G.ajouterArcValue(s3, s4, 12);

G.ajouterArcValue(s4, s5, 10);

G.ajouterArcValue(s5, s6, 4);
G.ajouterArcValue(s5, s7, 7);

G.ajouterArcValue(s6, s7, 2);

G.ajouterArcValue(s7, s8, 8);
 
