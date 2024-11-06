class Enofilo:
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
