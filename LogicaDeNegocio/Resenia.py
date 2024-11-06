from LogicaDeNegocio.Vino import Vino
from LogicaDeNegocio.auxFunc import *
from datetime import date, datetime


class Resenia:
    def __init__(
        self,
        comentario: str,
        premium: bool,
        fechaResenia: date,
        puntaje: float,
        vino: Vino,
    ) -> None:
        self.comentario = comentario
        self.premium = premium
        self.fechaResenia = datetime.strptime(fechaResenia[:10], "%Y-%m-%d").date()
        self.puntaje = puntaje
        self.vino = vino
        self.vino.resenias.append(self)

    # Metodos GET

    def __get_comentario(self):
        return self.comentario

    def __get_premium(self):
        return self.premium

    def __get_fechaResenia(self):
        return self.fechaResenia

    def __get_puntaje(self):
        return self.puntaje

    # Metodos SET

    def __set_comentario(self, comentario):
        self.comentario = comentario

    def __set_premium(self, premium):
        self.premium = premium

    def __set_fechaResenia(self, fechaResenia):
        self.fechaResenia = fechaResenia

    def __set_puntaje(self, puntaje):
        self.puntaje = puntaje

    # Metodos de Negocio

    def sosDePeriodo(self, fechaDesde, fechaHasta):
        if (fechaDesde) < (self.fechaResenia) < (fechaHasta):
            return True
        else:
            return False

    def sosDeSommelier(self):
        if self.premium == True:
            return True
        else:
            return False

    def sosDeEnofilo(self):
        if self.premium == False:
            return True
        else:
            return False

    def getPuntaje(self):
        return self.__get_puntaje()

    def obtenerFechaResenia(self):
        return self.__get_fechaResenia()
