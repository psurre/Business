import datetime

class Operation():

    def __init__(self):
        now = datetime.datetime.now()
        self.datecompta: str = str(now.strftime("%d/%m/%Y"))
        self.libsimple: str = ""
        self.libope: str = ""
        self.ref: str = ""
        self.info: str = ""
        self.typeope: str = ""
        self.cat: str = ""
        self.sscat: str = ""
        self.debit: int = 0
        self.credit: int = 0
        self.dateope: str = str(now.strftime("%d/%m/%Y"))
        self.dateval: str = str(now.strftime("%d/%m/%Y"))
        self.pointage: bool = False
        self.recurrent: bool = False

    def __init__(self, operation, recurrence):
        self.datecompta = operation[0]
        self.libsimple = operation[1]
        self.libope = operation[2]
        self.ref = operation[3]
        self.info = operation[4]
        self.typeope = operation[5]
        self.cat  = operation[6]
        self.sscat = operation[7]
        self.debit = operation[8]
        self.credit = operation[9]
        self.dateope = operation[10]
        self.dateval = operation[11]
        if operation[12] == 0:
            self.pointage = False
        else:
            self.pointage = True
        self.recurrent = recurrence
        


