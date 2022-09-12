import csv, logging, localeFR
from Operation import Operation
from Compte import Compte

def lireFichierCSV():
    titrecolonnes = True
    listtitres: list(str) = []
    listope: list(Operation) = []
    try:
        fichier = '/tobeanalyzed/source.csv'
        with open(fichier, newline='') as source:
            data = csv.reader(source, delimiter=';')
            for element in data:
                if titrecolonnes:
                    listtitres = element.copy()
                    titrecolonnes = False
                else:
                    operation = Operation(element, False)
                    listope.append(operation)
            compte = Compte(listtitres, listope)
            source.close
    except FileNotFoundError:
        logging.error(localeFR.ERRFILENOTFOUND.format(fichier))
        return None
    return compte