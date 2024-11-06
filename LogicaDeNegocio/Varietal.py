class Varietal:
    def __init__(
        self, descripcion: str, porcentajeComposicion: int, tipoUva: str
    ) -> None:
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva

    # Metodos GET

    def __get_descripcion(self):
        return self.descripcion

    def __get_porcentajeComposicion(self):
        return self.porcentajeComposicion

    def __get_tipoUva(self):
        return self.tipoUva

    # Metodos SET

    def __set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def __set_porcentajeComposicion(self, porcentajeComposicion):
        self.porcentajeComposicion = porcentajeComposicion

    def __set_tipoUva(self, tipoUva):
        self.tipoUva = tipoUva

    # Metodos de Negocio

    def mostrarPorcentaje(self):
        return self.__get_porcentajeComposicion()

    def getDescripcion(self):
        return self.__get_descripcion()
