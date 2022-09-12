import csv, logging, localeFR, constants
from Operation import Operation
from Compte import Compte
from datetime import date

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

def joursRestants():
    data = {}
    datelimite = date(day=int(constants.DATELIMITE['day']), month=int(constants.DATELIMITE['month']), year=int(constants.DATELIMITE['year']))
    today = date.today()
    daytolimit = datelimite - today
    data['datelimite'] = datelimite.strftime("%d/%m/%Y")
    data['today'] = today.strftime("%d/%m/%Y")
    data['daytolimit'] = daytolimit.days
    return data