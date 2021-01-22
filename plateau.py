class Plateau:
    def __init__(self,n):
        self.n=n
        self.liste=[[2]*self.n for i in range (self.n)]
    
    def __str__(self):
        tempo = ["     A   B   C   D   E   F   G   H  "]
        for i, l in enumerate(list(map(self.list_to_str, self.liste))):
            tempo.append("   +---+---+---+---+---+---+---+---+")
            tempo.append(" " + str(i+1) + l)
            
        tempo.append("   +---+---+---+---+---+---+---+---+")
        return "\n".join(tempo)

        #return "\n".join(["".join(str(elem)) for elem in self.liste])
    
    def initialisation(self):
        self.liste[3][4]=0
        self.liste[3][3]=1
        self.liste[4][3]=0
        self.liste[4][4]=1
        return self
    
    #maquillage
    def list_to_str(self,l):
        """
        input:
        liste avec valeur, variable interne
        """
        res=[]
        for e in l:
            if e==2:
                res.append(" ")
            elif e==1:
                res.append("X")
            else:
                res.append("O")
        return " | "+" | ".join(res)+" |"
    
    """def bord(self):
        tempo = ["     A   B   C   D   E   F   G   H  "]
        for i, l in enumerate(list(map(self.list_to_str, self.liste))):
            tempo.append("   +---+---+---+---+---+---+---+---+")
            tempo.append(" " + str(i+1) + l)
            
        tempo.append("   +---+---+---+---+---+---+---+---+")
        return "\n".join(tempo)"""

    def add_pion(self,x,y,couleur):
        self.liste[x][y]=couleur
        return self


    def add_blanc(self, x,y):
        self.add_pion(x,y,1)
        return self
    
    def add_noir(self, x,y):
        self.add_pion(x,y,0)
        return self

    def flip(self, x, y):
        self.liste[x][y]=abs(self.liste[x][y]-1)
        return self


"""l=Plateau(8)
 
print(l, "\n")
print(l.initialisation(), "\n")
print(l)"""

"""print(l.add_blanc(3,2), "\n")
print(l.add_noir(4,2), "\n")

print(l.flip(3,2),"\n")"""