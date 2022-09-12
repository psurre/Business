import logging
from Operation import Operation

class Compte():

    def __init__(self, headers, operations):
        self.intitule: str = "Compte chèque Banque Populaire"
        self.numero: int = 0
        self.proprio: str = "Patrick et Maud"
        self.type: str = "Courant"
        self.headers: list(str) = []
        self.operations: list(Operation) = []
        logging.debug(self.intitule)
        self.headers = headers.copy()
        for operation in operations:
            self.operations.append(operation)

    def afficherCompte(self):
        logging.debug(f"En têtes :")
        for entete in self.headers:
            logging.debug(f"- {entete}")
        for operation in self.operations:
            logging.debug (f"{operation.datecompta} - {operation.libsimple}")