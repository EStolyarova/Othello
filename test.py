from plateau import *
from engine import *

# On met sur la tableau le plateau vide sans pions
e = Engine()
p = Plateau(8)
print(p,"\n")

# on met les 4 pions sur le plateau et on affiche
p.initialisation()
print(p,"\n")

# la boucle pour 5 tours
for i in range(1, 64):
    if i%2 == 0:
        e.get_coordianate_blanc()
        p.add_blanc(e.x,e.y)
        print(p,"\n")
        l=e.coordinate_to_flip(p.liste)
        for elem in l:
            p.flip(elem[0], elem[1])
        print(p,"\n")
    else:
        e.get_coordianate_noir()
        p.add_noir(e.x,e.y)
        print(p,"\n")
        l=e.coordinate_to_flip(p.liste)
        for elem in l:
            p.flip(elem[0], elem[1])
        print(p,"\n")