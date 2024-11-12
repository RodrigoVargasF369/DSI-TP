from LogicaDeNegocio.InterfaceIterador import InterfaceIterador

class IteradorVino(InterfaceIterador):

    vinos = []
    posicion: int

    def __init__(self, objetos):
        self.vinos = objetos

    def getVinos(self):
        print(self.vinos)

    def primero(self):
        self.posicion = 0

    def haterminado(self):
        if self.posicion < len(self.vinos):
            return True
        else:
            return False
    def getActual(self,fechaDesde, fechaHasta,tipoResenia):
        if self.cumpleFiltro(fechaDesde, fechaHasta, tipoResenia):
            return self.vinos[self.posicion]
        return None

    def cumpleFiltro(self, fechaDesde, fechaHasta, tipoResenia):
        return self.vinos[self.posicion].tenesReseniasDeTipoEnPeriodo(fechaDesde, fechaHasta, tipoResenia)

    def siguiente(self):
        self.posicion += 1