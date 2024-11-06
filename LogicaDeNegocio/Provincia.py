from LogicaDeNegocio.Pais import Pais


class Provincia:
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
