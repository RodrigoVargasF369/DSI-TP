from LogicaDeNegocio.Provincia import Provincia, Pais


class RegionVitivinicola:
    def __init__(self, descripcion: str, nombre: str, provincia: Provincia) -> None:
        self.descripcion = descripcion
        self.nombre = nombre
        self.provincia = provincia
        self.provincia._regiones.append(self)

    # Metodos GET

    def __get_descripcion(self):
        return self.descripcion

    def __get_nombre(self):
        return self.nombre

    def __get_provincia(self):
        return self.provincia

    # Metodos SET

    def __set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def __set_nombre(self, nombre):
        self.nombre = nombre

    def __set_provincia(self, provincia):
        self.provincia = provincia

    # Metodos de Negocio

    def obtenerPais(self):
        return self.provincia.obtenerPais()

    def obtenerDescripcion(self):
        return self.__get_descripcion()

    def obtenerProvincia(self):
        return self.provincia

    def getNombre(self):
        return self.__get_nombre()
