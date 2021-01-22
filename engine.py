class Engine:


    def __init__(self):
        self.x=100
        self.y=100


        
    def get_coordianate_blanc(self):
        # creation du dictionnaire de matching entre
        # les coordonnes donnees par le joueur
        # et les coordonnees x et y numeriques
        list1 = list("12345678")
        list2 = list("ABCDEFGH")
        list3 = [i+j for i in list1 for j in list2]
        list4 = [(i, j) for i in range(len(list1)) for j in range(len(list2))]
        dic_matching = dict()
        for i in range(64):
            dic_matching[list3[i]] = list4[i]

        # demander les coordonnees (en str)
        print("c'est le tour du joueur blanc (X) \n")
        tempo = input("Donner la position du pion")
        self.x = dic_matching[tempo][0]
        self.y = dic_matching[tempo][1]
        return self

    def get_coordianate_noir(self):
        # creation du dictionnaire de matching entre
        # les coordonnes donnees par le joueur
        # et les coordonnees x et y numeriques
        list1 = list("12345678")
        list2 = list("ABCDEFGH")
        list3 = [i+j for i in list1 for j in list2]
        list4 = [(i, j) for i in range(len(list1)) for j in range(len(list2))]
        dic_matching = dict()
        for i in range(64):
            dic_matching[list3[i]] = list4[i]
        # demander les coordonnees (en str)
        print("c'est le tour du joueur noir (O) \n")
        tempo = input("Donner la position du pion")
        self.x = dic_matching[tempo][0]
        self.y = dic_matching[tempo][1]
        return self

    def check_right(self,pions):
    
        """
        input:
        pions:liste de listes
        x:coorodnnée x
        y:coordonnéé y
        output:
        liste_right: contient liste de coordonnées à changer.
        """
    
        liste_right=[]
        if self.y==7:
            pass
        else:

            i=self.y+1
            #la boucle vérifie la valeur(couleur) des cases se trouvant après y si elle contraire de la valeur de la case(x,y)
            
            while pions[self.x][i]==abs(pions[self.x][self.y]-1) and i<=8:
                i=i+1
                liste_right.append((self.x, i-1))
            
            # on ajoute à la liste le tuple contenant la coordonnée et la 
            #valeur de la derinère case causant la sortie de la boucle
            
            liste_right.append((self.x, i, pions[self.x][i]))
            
            #on teste la valeur du dernier élement de la liste, 
            #  si elle égale à la valeur du joueur en cours 
            
            if liste_right[-1][2]==pions[self.x][self.y]:
            
            #on  récupère la liste des coordonnées à changer lorsque le test est True
                liste_right=liste_right[:-1]
            #si faut on réinitialise la liste.
            else:
                liste_right=[]
        return liste_right

    def check_left(self,pions):
        liste_left=[]
        if self.y==0:
            pass
        else:

            i=self.y-1
            while pions[self.x][i]==abs(pions[self.x][self.y]-1) and i>=0:
                i=i-1
                liste_left.append((self.x, i+1))
            liste_left.append((self.x, i, pions[self.x][i]))
            
            if liste_left[-1][2]==pions[self.x][self.y]:
            
            #on  récupère la liste des coordonnées à changer lorsque le test est True
                liste_left=liste_left[:-1]
            #si faut on réinitialise la liste.
            else:
                liste_left=[]
        return liste_left

    def check_up(self,pions):
        
        
        liste_up=[]

        if self.x==0:
            pass
        else:
            i=self.x-1
            #la boucle vérifie la valeur(couleur) des cases se trouvant après y si elle contraire de la valeur de la case(x,y)
            while pions[i][self.y]==abs(pions[self.x][self.y]-1) and i>=0:
                i=i-1
                liste_up.append((i+1, self.y))
            # on ajoute à la liste le tuple contenant la coordonnée et la 
            #valeur de la derinère case causant la sortie de la boucle
            liste_up.append((i, self.y, pions[i][self.y]))
            #on teste la valeur du dernier élement de la liste, 
            #  si elle égale à la valeur du joueur en cours 
            if liste_up[-1][2]==pions[self.x][self.y]:
            #on  récupère la liste des coordonnées à changer lorsque le test est True
                liste_up=liste_up[:-1]
            #si faut on réinitialise la liste.
            else:
                liste_up=[]
        return liste_up

    def check_down(self,pions):
        liste_down=[]
        if self.x==7:
            pass
        else:

            i=self.x+1
            
            #la boucle vérifie la valeur(couleur) des cases se trouvant après y si elle contraire de la valeur de la case(x,y)
            while pions[i][self.y]==abs(pions[self.x][self.y]-1) and i<=6:
                i=i+1
                liste_down.append((i-1, self.y))

            liste_down.append((i, self.y, pions[i][self.y]))
            if liste_down[-1][2]==pions[self.x][self.y]:
            #on  récupère la liste des coordonnées à changer lorsque le test est True
                liste_down=liste_down[:-1]
            #si faut on réinitialise la liste.
            else:
                liste_down=[]
        return liste_down


    def check_DR(self,pions):
        liste_DR=[]
        if self.x==7 or self.y==7:
            pass
        else:

            i=self.x+1
            j=self.y+1
                
            while pions[i][j]==abs(pions[self.x][self.y]-1) and i<=8 and j<=8:
                i=i+1
                j+=1
                liste_DR.append((i-1, j-1))
            
            liste_DR.append((i, j, pions[i][j]))
            
            if liste_DR[-1][2]==pions[self.x][self.y]:
            
                liste_DR=liste_DR[:-1]
            else:
                liste_DR=[]
        return liste_DR

    def check_DL(self,pions):
        liste_DL=[]
        if self.x==7 or self.y==0:
            pass
        else:

            i=self.x+1
            j=self.y-1
            
                    
            while pions[i][j]==abs(pions[self.x][self.y]-1) and i<=8 and j>=0:
                i=i+1
                j-=1
                liste_DL.append((i-1, j+1))
            
            liste_DL.append((i, j, pions[i][j]))
            
            if liste_DL[-1][2]==pions[self.x][self.y]:
            
                liste_DL=liste_DL[:-1]
            else:
                liste_DL=[]
        return liste_DL

    def check_UR(self,pions):
        liste_UR=[]    
        if self.x==0 or self.y==7:
            pass
        else:
            i=self.x-1
            j=self.y+1
           
            
            while pions[i][j]==abs(pions[self.x][self.y]-1) and i>=0 and j<=8:
                i=i-1
                j=j+1
                liste_UR.append((i+1, j-1))
            
            liste_UR.append((i, j, pions[i][j]))
            
            if liste_UR[-1][2]==pions[self.x][self.y]:
            #on  récupère la liste des coordonnées à changer lorsque le test est True
                liste_UR=liste_UR[:-1]
            #si faut on réinitialise la liste.
            else:
                liste_UR=[]
        return liste_UR
    
    def check_UL(self,pions):
        liste_UL=[]
        if self.x==0 or self.y==0:
            pass
        else:    
            i=self.x-1
            j=self.y-1
            
            
            while pions[i][j]==abs(pions[self.x][self.y]-1) and i>=0 and j>=0:
                i=i-1
                j=j-1
                liste_UL.append((i+1, j+1))
            
            liste_UL.append((i, j, pions[i][j]))
            
            if liste_UL[-1][2]==pions[self.x][self.y]:
            #on  récupère la liste des coordonnées à changer lorsque le test est True
                liste_UL=liste_UL[:-1]
            #si faut on réinitialise la liste.
            else:
                liste_UL=[]
        return liste_UL

    def coordinate_to_flip(self,pions):
        tempo_liste=[]
        tempo_liste.extend(self.check_down(pions))
        tempo_liste.extend(self.check_left(pions))
        tempo_liste.extend(self.check_right(pions))
        tempo_liste.extend(self.check_up(pions))
        tempo_liste.extend(self.check_UL(pions))
        tempo_liste.extend(self.check_UR(pions))
        tempo_liste.extend(self.check_DR(pions))
        tempo_liste.extend(self.check_DL(pions))
        return tempo_liste


        
