from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..Persistencia.Persistencia import Base

class Enofilo(Base):
    
    __tablename__ = 'enofilo'
    id = Column(Integer, primary_key=True)
    apellido = Column(String)
    nombre = Column(String)
    resenias = relationship("Resenia", back_populates="enofilo")

    def __init__(self, apellido: str, nombre: str) -> None:
        self.apellido = apellido
        self.nombre = nombre

    # Metodos GET

    def __get_apellido(self):
        return self.apellido

    def __get_nombre(self):
        return self.nombre

    # Metodos SET

    def __set_apellido(self, apellido):
        self.apellido = apellido

    def __set_nombre(self, nombre):
        self.nombre = nombre

    # Metodos de Negocio
