import argparse

touches = {
    "à": (5,3),
    "j": (4,3),
    "o": (3,3),
    "é": (2,3),
    "b": (2,3),
    "f": (2,3),
    "d": (2,3),
    "l": (3,3),
    "'": (4,3),
    "q": (5,3),
    "x": (5,3),
    "ç": (5,3),
    "a": (5,2),
    "i": (4,2),
    "e": (3,2),
    "u": (2,2),
    ",": (2,2),
    "p": (2,2),
    "t": (2,2),
    "s": (3,2),
    "r": (4,2),
    "n": (5,2),
    "^": (5,2),
    "z": (5,2),
    "k": (5,1),
    "y": (4,1),
    "è": (3,1),
    ".": (2,1),
    "w": (2,1),
    "g": (2,1),
    "c": (2,1),
    "m": (3,1),
    "h": (4,1),
    "v": (5,1),
}



def ListeDeTouches(doigtsUtiles,Rang):
    l = []
    for k, v in touches.items():
        if v[1] == Rang:
            if v[0] in doigtsUtiles:
                l.append(k)
    return l


def ListeDeMots(listeDeTouches,fichier):
    f = open("corpus_francais.txt", "r", encoding="utf_8")
    l = []
    for mot in f:
        cntr = 0
        mot = mot[:-1]
        for lettre in list(mot):
            if lettre in listeDeTouches:
                cntr += 1
        if cntr == len(mot):
            l.append(mot)
    f.seek(0)
    w = open(fichier, "w", encoding="utf_8")
    for i in l:
        w.write(i+"\n")
    w.close()
    f.close()


l = ["a","i","e","u","t","s","r","n"]
ai = ["a","u","t","n"]
ami = ["a","e","u","t","s","n"]
aai = ["a","i","u","t","r","n"]

parser = argparse.ArgumentParser()
parser.add_argument("touches", help="les touches sous forme d'une string sans espaces ni séparation")
parser.add_argument("fichier", help="le nom du fichier devant contenir la liste de mots")
args = parser.parse_args()

touches = list(args.touches)
out = args.fichier

ListeDeMots(touches, out)