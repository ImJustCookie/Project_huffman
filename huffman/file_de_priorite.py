"""
bijour
"""
class FileDePrioriteVideErreur(Exception):
    pass

class ElementNonComparableErreur(Exception):
    pass

class FileDePriorite:
    """hello
    """
    file = []
    cle = None

    def __init__(self, elements =(), cle= lambda e:e):
        """ init"""
        self.cle = cle
        self.file = []
        for element in elements:
            self.enfiler(element)


    def est_comparable(self, element):
        try:
            toto = element < element
        except Exception :
            return False
        return True
    
    def est_comparable_avec_prev(self, element, prev):
        try:
            toto = element < prev
        except Exception :
            return False
        return True 
        

    @property
    def est_vide(self):
        """ est_vide"""
        return len(self.file) == 0

    def enfiler(self, element):
        """ enfile """
        if not self.est_comparable(element):
            raise ElementNonComparableErreur("nope ca marche po")
        
        if not self.est_vide:
            if not self.est_comparable_avec_prev(element, self.element):
                raise ElementNonComparableErreur("nope ca marche po prev")


        i = 0
        while i < len(self.file) and self.cle(element) >= self.cle(self.file[i]):
            i+=1
        self.file.insert(i,element)

    def defiler(self):
        """ defile """
        if self.est_vide:
            raise FileDePrioriteVideErreur("impossible de defiler une file vide")
        
        return self.file.pop(0)

    @property
    def element(self):
        """ retourne l'element le plus prio"""
        if self.est_vide:
            raise FileDePrioriteVideErreur("impossible de recuperer un element d'une file vide")
        
        return self.file[0]


    def __repr__(self):
        """ la methode de repr"""
        return f"FileDePriorite(({', '.join(iter([str(element) for element in self.file ]))}))"

    def __iter__(self):
        """ la methode pour string l'objet"""
        return iter(self.file)

    def __eq__(self, value):
        if type(value) == type(self):
            if len(self) != len(value):
                return False
            
            return self.file == value.file
        else :
            return False
    
    def __len__(self):
        return len(self.file)
    