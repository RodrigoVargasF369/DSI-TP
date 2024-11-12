from LogicaDeNegocio.InterfaceIterador import InterfaceIterador

class IteradorResenia(InterfaceIterador):

    resenias = []
    posicion: int

    def __init__(self, objetos):
        self.resenias = objetos

    def primero(self):
        self.posicion = 0

    def haterminado(self):
        if self.posicion < len(self.resenias):
            return True
        else:
            return False
        
    def getActual(self,fechaDesde,fechaHasta):
        return self.cumpleFiltro(fechaDesde,fechaHasta)

    def cumpleFiltro(self,fechaDesde,fechaHasta):
        return self.resenias[self.posicion].sosDePeriodo(fechaDesde,fechaHasta) and self.resenias[self.posicion].sosDeSommelier()

    def siguiente(self):
        self.posicion += 1
