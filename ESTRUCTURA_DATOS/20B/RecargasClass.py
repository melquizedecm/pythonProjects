from datetime import datetime

class Recargas:

    def __init__(self, numero, compania, monto):
        self.numero=numero
        self.compania=compania
        self.monto=monto
        self.hora=datetime.now()
    def recargas(self):
        pass

