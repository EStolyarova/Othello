from plateau import *

class Engine:


    def __init__(self):
        self.x=100
        self.y=100


        
    def get_coordianate_blanc(self):
        print("c'est le tour du joueur blanc \n")
        self.x=int(input("Donnez la position x"))
        self.y=int(input("Donnez la position y"))
        return self

    def get_coordianate_noir(self):
        print("c'est le tour du joueur noir \n")
        self.x=int(input("Donnez la position x"))
        self.y=int(input("Donnez la position y"))
        return self

    def check_right(pions, x, y):
    
    """
    input:
    pions:liste de listes
    x:coorodnnée x
    y:coordonnéé y
     
     
    output:
    
    liste_right: contient liste de coordonnées à changer.
    """
    i=y+1
    liste_right=[]
    
    #la boucle vérifie la valeur(couleur) des cases se trouvant après y si elle contraire de la valeur de la case(x,y)
    
    while pions[x][i]==abs(pions[x][y]-1) and i<=8:
        i=i+1
        liste_right.append((x, i-1))
    
    # on ajoute à la liste le tuple contenant la coordonnée et la 
    #valeur de la derinère case causant la sortie de la boucle
    
    liste_right.append((x, i, pions[x][i]))
    
    #on teste la valeur du dernier élement de la liste, 
    #  si elle égale à la valeur du joueur en cours 
    
    if liste_right[-1][2]==pions[x][y]:
    
    #on  récupère la liste des coordonnées à changer lorsque le test est True
        liste_right=liste_right[:-1]
    #si faut on réinitialise la liste.
    else:
        liste_right=[]
    return liste_right



e=Engine()
p= Plateau(8)
p.initialisation()

e.get_coordianate_blanc()
p.add_blanc(e.x,e.y)
print(p)
        
