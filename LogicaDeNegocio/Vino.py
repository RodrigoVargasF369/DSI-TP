from LogicaDeNegocio.Varietal import Varietal
from LogicaDeNegocio.Bodega import Bodega
from typing import List
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from Persistencia.Persistencia import Base
from LogicaDeNegocio.IteradorResenia import IteradorResenia

class Vino(Base):
    __tablename__ = 'vino'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    aniada = Column(Integer)
    imagenEtiqueta = Column(String)
    notaDeCataBodega = Column(Float)
    precioARS = Column(Float)
    varietal_id = Column(Integer, ForeignKey('varietal.id'))
    bodega_id = Column(Integer, ForeignKey('bodega.id'))

    varietal = relationship("Varietal", back_populates="vinos", lazy="joined")
    bodega = relationship("Bodega", back_populates="vinos", lazy="joined")
    resenias = relationship("Resenia", back_populates="vino", lazy="joined") 

    def __init__(
        self,
        nombre: str,
        aniada: int,
        imagenEtiqueta: str,
        notaDeCataBodega: float,
        precioARS: float,
        varietal: Varietal,
        bodega: Bodega,
    ) -> None:
        self.nombre = nombre
        self.aniada = aniada
        self.imagenEtiqueta = imagenEtiqueta
        self.notaDeCataBodega = notaDeCataBodega
        self.precioARS = precioARS
        self.varietal = varietal
        self.bodega = bodega
        self.resenias = []


    # Metodos GET

    def __get_nombre(self):
        return self.nombre

    def __get_aniada(self):
        return self.aniada

    def __get_imagenEtiqueta(self):
        return self.imagenEtiqueta

    def __get_notaDeCataBodega(self):
        return self.notaDeCataBodega

    def __get_precioARS(self):
        return self.precioARS

    def __get_varietal(self):
        return self.varietal

    def __get_bodega(self):
        return self.bodega

    def __get_resenias(self):
        return self.resenias

    # Metodos SET

    def __set_nombre(self, nombre):
        self.nombre = nombre

    def __set_aniada(self, aniada):
        self.aniada = aniada

    def __set_imagenEtiqueta(self, imagenEtiqueta):
        self.imagenEtiqueta = imagenEtiqueta

    def __set_notaDeCataBodega(self, notaDeCataBodega):
        self.notaDeCataBodega = notaDeCataBodega

    def __set_precioARS(self, precioARS):
        self.precioARS = precioARS

    def __set_varietal(self, varietal):
        self.varietal = varietal

    def __set_bodega(self, bodega):
        self.bodega = bodega

    def __set_resenias(self, resenias):
        self.resenias = resenias

    def crearIterador(self, resenias):
        return IteradorResenia(resenias)

    # Metodos de Negocio

    def tenesReseniasDeTipoEnPeriodo(self, fechaDesde, fechaHasta, tipoResenia):

        iteradorResenia = self.crearIterador(self.__get_resenias())
        print(len(self.__get_resenias()))
        iteradorResenia.primero()

        while iteradorResenia.haterminado():
            if tipoResenia == "Sommelier":
                if iteradorResenia.getActual(fechaDesde,fechaHasta):
                    return True
            iteradorResenia.siguiente()

        """
        for resenia in self.__get_resenias():
            if tipoResenia == "Sommelier":
                if (
                    resenia.sosDePeriodo(fechaDesde, fechaHasta)
                    and resenia.sosDeSommelier()
                ):
                    return True
            elif tipoResenia == "Normal":
                if (
                    resenia.sosDePeriodo(fechaDesde, fechaHasta)
                    and resenia.sosDeEnofilo()
                ):
                    return True
        return False
             """
    def getNombre(self):
        return self.__get_nombre()

    def getPrecio(self):
        return self.__get_precioARS()

    def buscarInfoBodega(self):
        nombreRegionVitivinicola, nombrePais = self.bodega.obtenerRegionPais()
        nombreBodega = self.bodega.getNombre()
        return nombreBodega, nombreRegionVitivinicola, nombrePais

    def buscarInfoVarietal(self):
        return self.varietal.getDescripcion()

    def calcularPromedioClasificacionSommelierEnPeriodo(self, fechaDesde, fechaHasta):
        puntaje = 0
        cantidad = 0
        for resenia in self.resenias:
            if (
                resenia.sosDePeriodo(fechaDesde, fechaHasta)
                and resenia.sosDeSommelier()
            ):
                puntaje += resenia.getPuntaje()
                cantidad += 1
        return self.calcularPromedio(puntaje, cantidad)

    def calcularPromedioClasificacionEnofiloEnPeriodo(self, fechaDesde, fechaHasta):
        puntaje = 0
        cantidad = 0
        for resenia in self.resenias:
            if resenia.sosDePeriodo(fechaDesde, fechaHasta) and resenia.sosDeEnofilo():
                puntaje += resenia.getPuntaje()
                cantidad += 1
        return self.calcularPromedio(puntaje, cantidad)

    def calcularPromedio(self, suma, cantidad):
        return round((suma / cantidad), 2) if cantidad != 0 else 0
