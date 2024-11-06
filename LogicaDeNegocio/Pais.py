class Pais:
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
