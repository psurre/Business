import csv, logging, localeFR, constants, json
from Operation import Operation
from Compte import Compte
from datetime import date, datetime

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

def persistKmsRestants(infos):
    fichier = f"{constants.PERSISTDIR}/{constants.KMSRESTANTSFILE}"
    datewrote = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    datatowrite = {
        "joursrestants": infos[0],
        "kmsparjour": infos[1],
        "horodatage": datewrote
    }
    try:
        with open(fichier, 'r+') as lecture:
            datalues = lecture.read()  
            dataluesjson = json.loads(datalues)
            dataluesjson['historique'].append(datatowrite)
            lecture.seek(0)
            json.dump(dataluesjson, lecture)
            lecture.truncate()
            lecture.close()
    except FileNotFoundError:
        logging.error(f"Le fichier {fichier} est introuvable.")
        return False
    except json.JSONDecodeError:
        logging.error(f"Erreur dans la sérialisation - désérialisation JSON")
        return False
    return True