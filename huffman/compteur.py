""" Module proposant la classe Compteur """
from typing import TypeVar, Callable
TypeGeneral = TypeVar('TypeGeneral')

class Compteur:
    """ Compteur permet d'avoir des statistiques (nombre d'occurences) sur
des éléments hashables

    arguments:
    val_init -- dictionnaire(element, nb_occurences) qui permet d'initialiser
le compteur à sa création
    """

    def __init__(self, val_init: dict[TypeGeneral, int] = None):
        if val_init is None :
            self.dico = {}
        else :
            self.dico = dict(val_init.items())#{ k:v for (k,v) in val_init.items() }

    def incrementer(self, element: TypeGeneral) -> None:
        """ca incremente """
        if element in self.dico:
            self.dico[element] += 1
        else:
            self.dico[element] = 1

    def fixer(self, element: TypeGeneral, nb_occurences: int) -> None:
        """ ca fixe """
        self.dico[element] = nb_occurences


    def nb_occurrences(self, element: TypeGeneral) -> int:
        """ca donne nb_occ """
        if element in self.dico:
            return self.dico[element]
        return 0

    def elements(self) -> set[TypeGeneral]:
        """ retourne les keys"""
        return set (self.dico.keys())


    def element_filtre(self, filtre : Callable[[int],bool]) -> set[TypeGeneral]:
        return {k for (k,v) in self.dico.items() if filtre(v)}

    
    def elements_moins_frequents(self) -> set[TypeGeneral]:
        """retourne tous les elements les moins frequents

        resultat: un ensemble contenant les éléments les moins fréquents
        """
        return self.element_filtre( lambda v : v == min(self.dico.values()))

    
    def elements_plus_frequents(self) -> set[TypeGeneral]:
        """retourne tous les elements les plus frequents

        resultat: un ensemble contenant les éléments les plus fréquents
        """
        return self.element_filtre( lambda v : v == max(self.dico.values()))


    def elements_par_nb_occurrences(self) -> dict[int, set[TypeGeneral]]:
        """retourne pour chaque nombre d'occurences présents dans compteur
les éléments qui ont ces nombres d'occurences

        resultat: un dictionnaire dont les clés sont les nombres d'occurences
et les valeurs des ensembles d'éléments qui ont ce nombre d'occurences"""
        temp = {}
        for k,val in self.dico.items():
            if val in temp:
                temp[val].add(k)
            else:
                temp[val]=set([k])


        return temp


def main():
    """Tests unitaires du module"""
    def ok_ko_en_str(booleen):
        return "OK" if booleen else "KO"

    def ok_ko(fct, resultat_attendu, *param):
        """mini fonction de TU"""
        res = fct.__name__ + ' : '
        res = res + ok_ko_en_str(fct(*param) == resultat_attendu)
        print(res)

    cpt1 = Compteur()
    cpt1.incrementer('a')
    cpt1.incrementer('a')
    cpt1.incrementer('b')
    cpt1.incrementer('c')
    cpt1.incrementer('c')
    cpt1.incrementer('c')
    cpt1.incrementer('d')

    ok_ko(Compteur.nb_occurrences, 2, cpt1, 'a')
    ok_ko(Compteur.elements, {'a', 'b', 'c', 'd'}, cpt1)
    ok_ko(Compteur.elements_moins_frequents, {'b', 'd'}, cpt1)
    ok_ko(Compteur.elements_plus_frequents, {'c'}, cpt1)
    ok_ko(Compteur.elements_par_nb_occurrences, {1: {'b', 'd'}, 2: {'a'}, 3: {'c'}}, cpt1)

if __name__ == "__main__":
    main()
