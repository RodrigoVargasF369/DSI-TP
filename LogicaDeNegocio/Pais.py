from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Persistencia.Persistencia import Base

class Pais(Base):

    __tablename__ = 'pais'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)

    provincias = relationship("Provincia", back_populates="pais")

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._provincias = []

    # Metodos GET

    def __get_nombre(self):
        return self.nombre

    def __get_provincias(self):
        return self._provincias

    # Metodos SET

    def __set_nombre(self, nombre):
        self.nombre = nombre

    # Metodos de Negocio

    def agregarProvincia(self, provincia):
        self._provincias.append(provincia)

    def getNombre(self):
        return self.__get_nombre()
