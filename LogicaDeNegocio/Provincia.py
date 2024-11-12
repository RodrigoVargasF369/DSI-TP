from LogicaDeNegocio.Pais import Pais
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..Persistencia.Persistencia import Base

class Provincia:

    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    pais_id = Column(Integer, ForeignKey('pais.id'))
    
    pais = relationship("Pais", back_populates="provincias")
    regiones = relationship("RegionVitivinicola", back_populates="provincia")

    def __init__(self, nombre: str, pais: Pais) -> None:
        self.nombre = nombre
        self.pais = pais
        self._regiones = []
        self.pais._provincias.append(self)

    # Metodos GET

    def __get_nombre(self):
        return self.nombre

    def __get_pais(self):
        return self.pais

    def __get_regiones(self):
        return self._regiones

    # Metodos SET

    def __set_nombre(self, nombre):
        self.nombre = nombre

    def __set_pais(self, pais):
        self.pais = pais

    # Metodos de Negocio

    def agregarRegion(self, region):
        self._regiones.append(region)

    def obtenerPais(self):
        return self.pais.getNombre()
