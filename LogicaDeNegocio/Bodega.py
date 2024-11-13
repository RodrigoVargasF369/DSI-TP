from LogicaDeNegocio.RegionVitivinicola import RegionVitivinicola
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Persistencia.Persistencia import Base

class Bodega(Base):

    __tablename__ = 'bodega'
    id = Column(Integer, primary_key=True)
    coordenadasUbicacion = Column(String)
    descripcion = Column(String)
    historia = Column(String)
    nombre = Column(String)
    periodoActualizacion = Column(String)
    region_id = Column(Integer, ForeignKey('region_vitivinicola.id'))

    regionVitivinicola = relationship("RegionVitivinicola", back_populates="bodegas", lazy="joined")
    vinos = relationship("Vino", back_populates="bodega")

    def __init__(
        self,
        coordenadasUbicacion: str,
        descripcion: str,
        historia: str,
        nombre: str,
        periodoActualizacion: str,
        regionVitivinicola: RegionVitivinicola,
    ) -> None:
        self.coordenadasUbicacion = coordenadasUbicacion
        self.descripcion = descripcion
        self.historia = historia
        self.nombre = nombre
        self.periodoActualizacion = periodoActualizacion
        self.regionVitivinicola = regionVitivinicola

    # Metodos GET

    def __get_coordenadasUbicacion(self):
        return self.coordenadasUbicacion

    def __get_descripcion(self):
        return self.descripcion

    def __get_historia(self):
        return self.historia

    def __get_nombre(self):
        return self.nombre

    def __get_periodoActualizacion(self):
        return self.periodoActualizacion

    # Metodos SET

    def __set_coordenadasUbicacion(self, coordenadasUbicacion):
        self.coordenadasUbicacion = coordenadasUbicacion

    def __set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def __set_historia(self, historia):
        self.historia = historia

    def __set_nombre(self, nombre):
        self.nombre = nombre

    def __set_periodoActualizacion(self, periodoActualizacion):
        self.periodoActualizacion = periodoActualizacion

    # Metodos de Negocio

    def getNombre(self):
        return self.__get_nombre()

    def obtenerRegionPais(self):
        nombrePais = self.regionVitivinicola.obtenerPais()
        nombreRegionVitivinicola = self.regionVitivinicola.getNombre()
        return nombreRegionVitivinicola, nombrePais
