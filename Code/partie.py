import time
from random import randrange, choice, random
import Code.personnage as perso
import threading
import os

path = os.getcwd()
path += "\\Data"
os.chdir(path)


class Partie(list):
    """dans self sera contenu les ennemis avec les joueurs (à la position prévue)"""

    def __init__(self, l, h):
        super().__init__()
        self.__h = h + 2  # Pour compenser les False qui apparaissent
        self.__l = l + 2
        self.__generation_map()
        self.map = self.get_map()
        self.joueurs = {}
        self.ennemis = {}
        self.limite_spawn = 5
        self.multi = False

    def __generation_map(self):
        for x in range(self.l):
            self.append([])
            for y in range(self.h):
                if x == 0 or x == self.l - 1 or y == 0 or y == self.h - 1:
                    self[x].append(False)
                else:
                    self[x].append(None)

    def new_player(self, nom, classe):
        differentes_classes = {'epeiste': perso.Epeiste,
                               'garde': perso.Garde,
                               'sorcier': perso.Sorcier,
                               'druide': perso.Druide}
        classe = differentes_classes[classe]
        if not self.multi:
            joueur = classe(self, (self.l - self.l // 4, self.h // 2), nom)
        else:
            pass  # On l'implémentera plus tard
        return

    @property
    def h(self):
        return self.__h

    @property
    def l(self):
        return self.__l

    def get_map(self):
        """Ca permet de faire le lien entre personnage et partie (en appelant la map dans personnage)"""
        return self

    def spawn_ennemi(self, niveau):
        if perso.Ennemi.compteur < self.limite_spawn:
            proba = random()
            if proba < 0.4:
                self.spawn_squelette(niveau)
            elif 0.4 <= proba < 0.8:
                self.spawn_crane(niveau)
            elif 0.8 <= proba < 0.9:
                self.spawn_invocateur(niveau)
            else:
                self.spawn_armure(niveau)
            return True

    def spawn_squelette(self, niveau):
        cases_possibles = []
        for i in range(self.h):
            for j in range(self.l):
                if self[j][i] is None:
                    cases_possibles.append((i, j))
        x, y = choice(cases_possibles)
        ennemi = perso.Squelette(self, (x, y), niveau)

    def spawn_crane(self, niveau):
        cases_possibles = []
        for i in range(self.h):
            for j in range(self.l):
                if self[j][i] is None:
                    cases_possibles.append((i, j))
        x, y = choice(cases_possibles)
        ennemi = perso.Crane(self, (x, y), niveau)

    def spawn_armure(self, niveau):
        cases_possibles = []
        for i in range(self.h):
            for j in range(self.l):
                if self[j][i] is None:
                    cases_possibles.append((i, j))
        x, y = choice(cases_possibles)
        ennemi = perso.Armure(self, (x, y), niveau)

    def spawn_invocateur(self, niveau):
        cases_possibles = []
        for i in range(self.h):
            for j in range(self.l):
                if self[j][i] is None:
                    cases_possibles.append((i, j))
        x, y = choice(cases_possibles)
        ennemi = perso.Invocateur(self, (x, y), niveau)

    def open_save(self):
        pass

    @staticmethod
    def write_save():
        # Bon donc ici on met une base de données ?
        # On peut très très facilement rester sur du txt
        # On stock chaque joueur sans inventaire
        # On stock ensuite l'inventaire
        # On finit pas simplement stocker les variables de classes et tout est stocké
        # Autrement je te laisse me proposer une modélisation de bdd
        # Après utiliser sqlite sur python c'est ez

        # On peut faire un BDD Joueur avec :
        # BDD : Joueurs
        # nom (PK), id_partie (FK), niveau, position, element inventaire 1, element inventaire 2, ...,
        # BDD : Partie
        # id_partie (PK), temps de jeu, nombre de mort, nb dennemis tués, nb de squelette tués, nb de crane tués, ...
        # Ca nous permettra, avec une simple requete, de récuperer ce quil faut sur le joueur...
        # Apres, on est pas obligé dimplémenter les BDD pour les saves, on peut les ajouter en
        # plus des saves, pour avoir un write_save et un write BDD sui supprimerait les anciennes
        # données dun joueurs pour en mettre de nouvelles... ca nous ferait 2 types de fichier,
        # et la BDD serait notamment utile pour un ScoreBoard, ou je ne sais quoi
        pass

    def action_mechant(self):
        """Cette fonction va tourner sur un thread avec une clock spécifique qui ralentira la cadence
        (comme dans bca en fait)"""
        i = 0
        avg = 0
        while True:
            print(self)
            t0_loop = time.time()
            while perso.Ennemi.compteur < 5:
                lv = list(self.joueurs.values())[0].niveau  # ça commence à être moche
                lvl = lv + randrange(-2, 3)
                if lvl <= 1:
                    lvl = 1
                self.spawn_ennemi(lvl)
            for mechant in self.ennemis.values():
                print(mechant.cible)
                if mechant.cible:
                    xs, ys = mechant.position
                    xc, yc = mechant.cible.position
                    if abs(xc - xs) == 1 or abs(yc - ys) == 1:  # Wesh j'suis trop con, faudrait une fonction "porté"
                        mechant.attaquer()
                        print("attaque")
                    else:
                        mechant.deplacement()
                        print("bouger")
                else:
                    mechant.deplacement()
                    print("bouger")
                mechant.agro()
            t_loop = time.time() - t0_loop
            avg += t_loop
            print(t_loop)
            if t_loop < 1:  # Les 5 ennemis vont agir à 1 Hz
                time.sleep(1 - t_loop)
            else:
                print('Too many computation in this loop')  # Meilleur ref
            i += 1
            print(i)
            if i == 10:
                break
        print(avg/i)

    def action_joueur(self):
        """Là je sais pas encore quoi faire, ça dépend grv de PyQt"""
        pass

    def __str__(self):
        canvas = ""
        for y in range(self.h):
            for x in range(self.l - 1):
                canvas += str(self[x][y]) + ", "
            canvas += str(self[self.l - 1][y])
            canvas += "\n"
        return canvas

    def run_thread(self):
        self.thread_ennemis = threading.Thread(target=self.action_mechant)
        if self.multi:
            pass
            #self.thread_TCP = threading.Thread(target=tcp_client)

if __name__ == '__main__':
    a = Partie(20, 10)
    print(a)
