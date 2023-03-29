import partie as prt
import personnage as p
import os

if __name__ == '__main__':
    path = os.getcwd()

    game = prt.Partie(10, 5)
    Link = p.Epeiste(game, (5, 5), 'Link', niveau=5)
    print(Link.vie)
    Link.vie += 5
    Link.vie -= Link.viemax
    print(Link.vie)