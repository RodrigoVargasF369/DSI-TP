from LogicaDeNegocio.IteradorVino import IteradorVino
from LogicaDeNegocio.Vino import Vino
from LogicaDeNegocio.InterfazExcel import InterfazExcel
from Persistencia.datosTest import datos
from datetime import datetime, date


class GestorRankingVinos:
    def __init__(
        self,
        fechaDesde: date,
        fechaHasta: date,
        tipoResenia: str,
        tipoVisualizacion: str,
        confirmacion: bool,
    ) -> None:
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.tipoResenia = tipoResenia
        self.tipoVisualizacion = tipoVisualizacion
        self.confirmacion = confirmacion

    # Metodos GET

    def __get_fechaDesde(self):
        return self.fechaDesde

    def __get_fechaHasta(self):
        return self.fechaHasta

    def __get_tipoResenia(self):
        return self.tipoResenia

    def __get_tipoVisualizacion(self):
        return self.tipoVisualizacion

    def __get_confirmacion(self):
        return self.confirmacion

    # Métodos SET

    def __set_fechaDesde(self, fechaDesde):
        self.fechaDesde = fechaDesde

    def __set_fechaHasta(self, fechaHasta):
        self.fechaHasta = fechaHasta

    def __set_tipoResenia(self, tipoResenia):
        self.tipoResenia = tipoResenia

    def __set_tipoVisualizacion(self, tipoVisualizacion):
        self.tipoVisualizacion = tipoVisualizacion

    def __set_confirmacion(self, confirmacion):
        self.confirmacion = confirmacion

    # Métodos de Negocio

    def opcionGenerarRankingVinos(self, PRV):
        # Recibe por parametros el propio gestor (self) y el objeto Pantalla (PRV)
        # Los objetos Pantalla y Gestor se pasan por parametro para poder utilizar
        # los métodos de uno en el otro
        PRV.solicitarSelFechaDesdeHasta(self)
        if not self.__get_fechaDesde() or not self.__get_fechaHasta():
            return

        PRV.solicitarSelTipoResenia(self)
        if not self.__get_tipoResenia():
            return

        PRV.solicitarSelTipoVisualizacion(self)
        if not self.__get_tipoVisualizacion():
            return

        PRV.solicitarConfirmacionGenResenia(self)
        if not self.__get_confirmacion():
            return
        # !La funcion datos() es el reemplazo de la base de datos
        vinos = datos()
        # vinos=datosejemplo()
        vinostipoPeriodo = self.tenesReseniaDeTipoEnPeriodo(vinos)
        # print(len(vinostipoPeriodo))
        # bodegasNombres, regionesBodegas, paisesBodegas, varietalDescripcion = self.buscarInfoBodegas()

        if self.tipoResenia == "Sommelier":
            vinosFinales = self.calcularPromedioClasificacionSommelierEnPeriodo(
                vinos, vinostipoPeriodo
            )
        elif self.tipoResenia == "Normal":
            vinosFinales = self.calcularPromedioClasificacionEnofiloEnPeriodo(
                vinos, vinostipoPeriodo
            )
        elif self.tipoResenia == "Amigos":
            print("Método no implementado")
        # print(len(vinosFinales))
        lista_vinos_ordenada = self.ordenarVinos(vinosFinales)
        lista_vinos_primeros_10 = lista_vinos_ordenada[:10]
        # print(lista_vinos_primeros_10)
        if self.tipoVisualizacion == "PDF":
            print("No implementado")
            self.fin_cu()
        elif self.tipoVisualizacion == "Excel":
            interfaz_excel = InterfazExcel()
            interfaz_excel.generarArchivo(
                lista_vinos_primeros_10,
                f"Ranking-Vinos{datetime.now().strftime('-%Y-%m-%d-%H-%M')}.xlsx",
                [
                    "Vino",
                    "Calificación",
                    "Precio",
                    "Bodega",
                    "Varietal",
                    "Región",
                    "País",
                ],
            )
            PRV.informarCreacion()
            self.fin_cu()
        elif self.tipoVisualizacion == "Pantalla":
            PRV.mostrarRankingPorPantalla(
                lista_vinos_primeros_10,
                f"Ranking Vinos {(datetime.now().strftime('-%Y-%m-%d-%H-%M')).replace('-', ' ')}",
                [
                    "Vino",
                    "Calificación",
                    "Precio",
                    "Bodega",
                    "Varietal",
                    "Región",
                    "País",
                ],
            )
            self.fin_cu()

    def tomarSelFechaDesde(self, fechaDesde):
        self.__set_fechaDesde(fechaDesde)

    def tomarSelFechaHasta(self, fechaHasta):
        self.__set_fechaHasta(fechaHasta)

    def tomarSelTipoResenia(self, tipoResenia):
        self.__set_tipoResenia(tipoResenia)

    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        self.__set_tipoVisualizacion(tipoVisualizacion)

    def tomarConfirmacionGenResenia(self, value):
        self.__set_confirmacion(value)

    def crearIterador(self, vinos):
        return IteradorVino(vinos)
    def tenesReseniaDeTipoEnPeriodo(self, vinos):

        vinostipoPeriodo = []
        # Definicion de variables con los valores de los atributos para acortar llamadas a métodos
        fechaDesde = self.__get_fechaDesde()
        fechaHasta = self.__get_fechaHasta()
        tipoResenia = self.__get_tipoResenia()

        iteradorVinos = self.crearIterador(vinos)
        iteradorVinos.primero()
        #print(len(vinos))

        while iteradorVinos.haterminado():
            vino = iteradorVinos.getActual(fechaDesde, fechaHasta, tipoResenia)
            #print(vino)
            if vino is not None:
                nombre = vino.getNombre()
                precio = vino.getPrecio()
                nombreBodega, nombreRegionVitivinicola, nombrePais = (
                    vino.buscarInfoBodega()
                )
                varietal = vino.buscarInfoVarietal()
                diccionarioVino = {
                    "nombre": nombre,
                    "precio": precio,
                    "nombreBodega": nombreBodega,
                    "nombreRegionVitivinicola": nombreRegionVitivinicola,
                    "nombrePais": nombrePais,
                    "varietal": varietal,
                }
                vinostipoPeriodo.append(diccionarioVino)

            iteradorVinos.siguiente()
        return vinostipoPeriodo

        """
        vinostipoPeriodo = []
        # Definicion de variables con los valores de los atributos para acortar llamadas a métodos
        fechaDesde = self.__get_fechaDesde()
        fechaHasta = self.__get_fechaHasta()
        for vino in vinos:
            if vino.tenesReseniasDeTipoEnPeriodo(
                fechaDesde, fechaHasta, self.__get_tipoResenia()
            ):
                nombre = vino.getNombre()
                precio = vino.getPrecio()
                nombreBodega, nombreRegionVitivinicola, nombrePais = (
                    vino.buscarInfoBodega()
                )
                varietal = vino.buscarInfoVarietal()
                diccionarioVino = {
                    "nombre": nombre,
                    "precio": precio,
                    "nombreBodega": nombreBodega,
                    "nombreRegionVitivinicola": nombreRegionVitivinicola,
                    "nombrePais": nombrePais,
                    "varietal": varietal,
                }
                vinostipoPeriodo.append(diccionarioVino)
        return vinostipoPeriodo
     """
    def calcularPromedioClasificacionSommelierEnPeriodo(self, vinos, vinostipoPeriodo):
        puntajes = []
        posicion = 0
        for vino in vinos:
            puntaje = vino.calcularPromedioClasificacionSommelierEnPeriodo(
                self.fechaDesde, self.fechaHasta
            )
            # print(puntaje)
            if puntaje > 0:
                puntajes.append(puntaje)
        for vino in vinostipoPeriodo:
            vino["puntaje"] = puntajes[posicion]
            posicion += 1
        return vinostipoPeriodo

    def calcularPromedioClasificacionEnofiloEnPeriodo(self, vinos, vinostipoPeriodo):
        puntajes = []
        posicion = 0
        for vino in vinos:
            puntaje = vino.calcularPromedioClasificacionEnofiloEnPeriodo(
                self.fechaDesde, self.fechaHasta
            )
            # print(puntaje)
            if puntaje > 0:
                puntajes.append(puntaje)
        for vino in vinostipoPeriodo:
            vino["puntaje"] = puntajes[posicion]
            posicion += 1
        return vinostipoPeriodo

    def ordenarVinos(self, vinostipoPeriodo):
        vinosOrdenados = sorted(
            vinostipoPeriodo, key=lambda x: x["puntaje"], reverse=True
        )
        return vinosOrdenados

    def fin_cu(self):
        return
